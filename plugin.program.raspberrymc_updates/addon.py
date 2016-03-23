"""
    Plugin for Launching Updates for the RaspberryMC

    MCUpdate: updates just kodi with the latest addons, does not overwrite user settings (unless conflicts with update) or favorites.
    ESROMUpdates: updates just Emulation Stations ROM files (adds new roms to system)
    AdultContent: if enabled will sync the Adult Content AddOns
    PreUpdates: will check and update the RaspberryMC Update addon
    Debugging: prevents log files from being cleared at start of each run

"""

# -*- coding: UTF-8 -*-
# main imports
import sys
import os
import xbmc
import xbmcgui
import xbmcaddon

# plugin constants
__plugin__ = "raspberrymc_updates"
__author__ = "raspberrymc"
__url__ = "http://www.raspberrymc.com"
__credits__ = "RaspberryMC"
__version__ = "1.0.0"
__settings__ = xbmcaddon.Addon(id='plugin.program.raspberrymc_updates')

dialog = xbmcgui.Dialog()

# addon settings values
PREUPDATE = __settings__.getSetting("preUpdate")
MCUPDATE = __settings__.getSetting("mcUpdate")
ESROMUPDATES = __settings__.getSetting("es-rom-updates")
ADULTCONTENT = __settings__.getSetting("adultcontent")
DEBUGGING = __settings__.getSetting("debug")


def clearLog():
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/clearlog.sh").read()


def premissionUpdates():
    os.system("sudo chmod 755 /home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/*")

def mcrestart():
    os.system("sudo systemctl restart mediacenter")

def preupdate():
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/preupdates.sh").read()
    premissionUpdates()
    xbmc.executebuiltin("Dialog.Close(busydialog)")
    dialog.notification("PreUpdate Notification", "Finish running PreUpdate")


def mcupdate():
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/mcupdates.sh").read()
    premissionUpdates()
    xbmc.executebuiltin("Dialog.Close(busydialog)")
    dialog.notification("Update Notification", "Media Center Update Completed", xbmcgui.NOTIFICATION_INFO, 5000)


def esromupdates():
    # TODO: test script, make exclude list for saved game data
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/esromupdates.sh").read()
    dialog.notification("Update Notification", "ES ROM Update Completed", xbmcgui.NOTIFICATION_INFO, 5000)
    xbmc.executebuiltin("Dialog.Close(busydialog)")

def adultcontent():
    # TODO: test script and exclude list
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/adultcontent.sh").read()
    dialog.notification("Update Notification", "Adult Content Update Completed", xbmcgui.NOTIFICATION_INFO, 5000)
    xbmc.executebuiltin("Dialog.Close(busydialog)")

def rmadultcontent():
    # TODO: rmadultcontent script
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/rmadultcontent.sh").read()
    dialog.notification("Update Notification", "Adult Content Removed", xbmcgui.NOTIFICATION_INFO, 5000)
    xbmc.executebuiltin("Dialog.Close(busydialog)")


premissionUpdates()

if DEBUGGING == "false":
    clearLog()

if PREUPDATE == "true":
    dialog.ok("Run PreUpdate", "Check for updates to the RaspberryMC Update Script Files")
    preupdate()
    __settings__.setSetting(id='preUpdate', value='false')


else:
    if dialog.yesno("Update Notification",
                    "It is recommended that you backup your settings before proceeding.  Do you want to continue?"):
        if MCUPDATE == "true":
            dialog.notification('Update Notifications', 'Starting Media Center Updates', xbmcgui.NOTIFICATION_INFO,
                                2500)
            mcupdate()

        if ESROMUPDATES == "true":
            dialog.notification('Update Notification', 'Running ES ROM Updates', xbmcgui.NOTIFICATION_INFO, 2500)
            esromupdates()

        if ADULTCONTENT == "true":
            dialog.notification('Update Notification', 'Starting Updates of Custom User Options', xbmcgui.NOTIFICATION_INFO, 2500)
            adultcontent()
            if dialog.yesno("Update Complete", "Restart required", "Do you want to continue?"):
                mcrestart()

        elif ADULTCONTENT == "false":
            dialog.notification('Removal Notification', 'Removing Adult Content', xbmcgui.NOTIFICATION_INFO, 2500)
            rmadultcontent()
            if dialog.yesno("Update Complete", "Restart required", "Do you want to continue?"):
                mcrestart()

    dialog.ok("Notification", "Update Complete")
