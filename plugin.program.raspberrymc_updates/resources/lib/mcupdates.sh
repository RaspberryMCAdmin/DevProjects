#!/bin/bash

# Copy osmc/kodi from cloud server
rclone copy -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" --exclude-from /home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/lib/mc-ignore-list.txt  update_gdrive:AMA_ES/home/osmc/.kodi /home/osmc/.kodi/

# sync Support/tools folder from cloud server
rclone copy -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" update_gdrive:AMA_ES/home/osmc/Support/tools/ /home/osmc/Support/tools/

# update RaspberryMC logo
rclone copy -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_updates/resources/logs/update-log.txt" update_gdrive:AMA_ES/home/osmc/Support/tools/images/OSMC.png /usr/share/kodi/addons/skin.osmc/media/OSMC.png

echo "MC Update Complete."
exit