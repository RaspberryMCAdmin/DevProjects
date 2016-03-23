#!/bin/bash
# Sync Emulation Station ROM files to cloud server
rclone copy -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" /opt/retrosmc update_gdrive:AMA_ES/opt/retrosmc

echo "Push Emulation Station ROM Update Complete."
exit