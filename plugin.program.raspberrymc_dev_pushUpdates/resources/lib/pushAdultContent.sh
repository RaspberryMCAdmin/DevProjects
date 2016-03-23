#!/bin/bash

# Push Adult Content addon to cloud server
rclone sync -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_dev_pushUpdates/resources/logs/update-log.txt" /home/osmc/.kodi/addons/plugin.video.uwc update_gdrive:AMA_ES/home/osmc/.kodi/addons/plugin.video.uwc

rclone sync -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_dev_pushUpdates/resources/logs/update-log.txt" /home/osmc/.kodi/addons/plugin.video.you.jizz update_gdrive:AMA_ES/home/osmc/.kodi/addons/plugin.video.you.jizz

echo "Update Sync Complete."
exit