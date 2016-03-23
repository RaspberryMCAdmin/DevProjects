#!/bin/bash

# Copy addonupdate/preupdate files to cloud server
rclone sync -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_dev_pushUpdates/resources/logs/update-log.txt" /home/osmc/.kodi/addons/plugin.program.raspberrymc_dev_updates/ update_gdrive:AMA_ES/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/

exit