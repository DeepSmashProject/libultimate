
   
# inside docker script
trap 'kill $(jobs -p)' EXIT

# 0. generate xorg.conf
# This is for OpenGL 4.6.0
BUS_ID=$(nvidia-xconfig --query-gpu-info | grep 'PCI BusID' -m 1 | sed -r 's/\s*PCI BusID : PCI:(.*)/\1/')
echo "BUS_ID=$BUS_ID"
sudo nvidia-xconfig -a --virtual=$RESOLUTION --allow-empty-initial-configuration --enable-all-gpus --busid $BUS_ID

# 1. launch X server
sudo Xorg $DISPLAY &
sleep 1  # wait for the server gets ready
# glxinfo | grep "OpenGL version"

# 2. start x11 and vnc connection
# to inspect logs in detail, use --verbose
x11vnc -display $DISPLAY -forever -rfbport 5900 &
sleep 2  # wait for the server gets ready

# 3. start noVNC
/usr/bin/websockify -D --web=/usr/share/novnc/ $NOVNC_PORT localhost:5900 &
sleep 2

# Run Ryujinx

# bash
/bin/bash
