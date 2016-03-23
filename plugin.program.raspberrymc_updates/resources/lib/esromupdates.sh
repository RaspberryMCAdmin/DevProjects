#!/bin/bash

# Sync RetroPie system and userdata files
rclone copy -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" update_gdrive:AMA_ES/opt/retrosmc /opt/retrosmc

# create exclude file for saved game data

echo "RetroPie Update Complete."
exit