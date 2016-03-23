#!/bin/bash

# Install Adult Content addon from cloud server
rclone copy -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" update_gdrive:AMA_ES/home/osmc/.kodi/addons/plugin.video.uwc /home/osmc/.kodi/addons/plugin.video.uwc

rclone copy -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" update_gdrive:AMA_ES/home/osmc/.kodi/addons/plugin.video.you.jizz /home/osmc/.kodi/addons/plugin.video.you.jizz

echo "Update Sync Complete."
exit