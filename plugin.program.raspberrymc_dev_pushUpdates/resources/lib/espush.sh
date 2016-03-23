#!/bin/bash

# Sync RetroPie load screen files to cloud server
rclone copy -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" /home/RetroPie update_gdrive:AMA_ES/home/RetroPie

# Sync RetroPie system and userdata files
rclone copy -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" /opt/retrosmc update_gdrive:AMA_ES/opt/retrosmc

echo "RetroPie Update Complete."
exit