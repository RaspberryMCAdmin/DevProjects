#!/bin/bash

# Copy osmc/kodi to cloud server
rclone sync --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_dev_pushUpdates/resources/logs/push-update-log.txt" --exclude-from /home/osmc/.kodi/addons/plugin.program.raspberrymc_dev_pushUpdates/resources/lib/mc-ignore-list.txt /home/osmc/.kodi/ update_gdrive:AMA_ES/home/osmc/.kodi

# sync Support/tools folder to cloud server
rclone sync -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_dev_pushUpdates/resources/logs/push-update-log.txt" /home/osmc/Support/tools/ update_gdrive:AMA_ES/home/osmc/Support/tools/

# push RaspberryMC logo
rclone sync -v --log-file="/home/osmc/.kodi/addons/plugin.program.raspberrymc_dev_pushUpdates/resources/logs/push-update-log.txt" /usr/share/kodi/addons/skin.osmc/media/OSMC.png update_gdrive:AMA_ES/home/osmc/Support/tools/images/OSMC.png

echo "Push MC Update Complete."
exit