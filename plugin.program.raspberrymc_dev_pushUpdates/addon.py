"""
    Plugin is for Developer use only.

    Plugin is used to push the latest RaspberryMC updates to the cloud server.

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
__plugin__ = "raspberrymc_dev_pushUpdates"
__author__ = "raspberrymc"
__url__ = "http://www.raspberrymc.com"
__credits__ = "RaspberryMC"
__version__ = "1.0.0"
__settings__ = xbmcaddon.Addon(id='plugin.program.raspberrymc_dev_pushUpdates')

dialog = xbmcgui.Dialog()

# addon settings values
MCUPDATE = __settings__.getSetting("push-mcUpdate")
ESUPDATES = __settings__.getSetting("push-es-updates")
ESROMUPDATES = __settings__.getSetting("push-es-rom-updates")
ADULTCONTENT = __settings__.getSetting("push-adultcontent")
DEBUGGING = __settings__.getSetting("debug")


def clearLog():
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_dev_pushUpdates/resources/lib/clearlog.sh").read()

def updatePrem():
    os.system("sudo chmod 755 /home/osmc/.kodi/addons/plugin.program.raspberrymc_dev_pushUpdates/resources/lib/*")

def mcrestart():
    os.system("sudo systemctl restart mediacenter")

def mcupdate():
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_dev_pushUpdates/resources/lib/mcpush.sh").read()
    xbmc.executebuiltin("Dialog.Close(busydialog)")
    dialog.notification("Push Notification", "Media Center Push Updates Finished", xbmcgui.NOTIFICATION_INFO, 5000)

def adultcontent():
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_dev_pushUpdates/resources/lib/pushAdultContent.sh").read()
    xbmc.executebuiltin("Dialog.Close(busydialog)")
    dialog.notification("Push Notification", "Adult Content Push Finished", xbmcgui.NOTIFICATION_INFO, 5000)

def esupdates():
    # TODO: test script, make exclude list for saved game data
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_dev_pushUpdates/resources/lib/espush.sh").read()
    dialog.notification("Push Notification", "ES Push Update Finished", xbmcgui.NOTIFICATION_INFO, 5000)
    xbmc.executebuiltin("Dialog.Close(busydialog)")

def esromupdates():
    # TODO: test script, make exclude list for saved game data
    xbmc.executebuiltin("ActivateWindow(busydialog)")
    os.popen("/home/osmc/.kodi/addons/plugin.program.raspberrymc_dev_pushUpdates/resources/lib/esrompush.sh").read()
    dialog.notification("Push Notification", "ES ROM Push Update Finished", xbmcgui.NOTIFICATION_INFO, 5000)
    xbmc.executebuiltin("Dialog.Close(busydialog)")

updatePrem()

if DEBUGGING == "false":
    clearLog()


if dialog.yesno("Push Notifications", "Push Updates will overwrite cloud server files!!!", "Do you want to continue?"):
    if MCUPDATE == "true":
        dialog.notification('Push Notifications', 'Pushing Media Center Updates', xbmcgui.NOTIFICATION_INFO, 7500)
        mcupdate()

    if ADULTCONTENT == "true":
        dialog.notification('Push Notifications', 'Pushing Adult Content Updates', xbmcgui.NOTIFICATION_INFO, 7500)
        adultcontent()

    if ESUPDATES == "true":
        dialog.notification('Push Notification', 'Pushing ES Updates', xbmcgui.NOTIFICATION_INFO, 7500)
        #esupdates()

    elif ESROMUPDATES == "true":
        dialog.notification('Push Notification', 'Pushing ES ROM Updates', xbmcgui.NOTIFICATION_INFO, 2500)
        #esromupdates()

    dialog.ok("Push Notification", "Push MediaCenter Updates Complete")
