
   
# inside docker script
trap 'kill $(jobs -p)' EXIT

# 0. generate xorg.conf
#BUS_ID=$(nvidia-xconfig --query-gpu-info | grep 'PCI BusID' | sed -r 's/\s*PCI BusID : PCI:(.*)/\1/')
# This is for OpenGL 4.6.0
nvidia-xconfig -a --virtual=$RESOLUTION --allow-empty-initial-configuration --enable-all-gpus --busid $BUS_ID

# 1. launch X server
Xorg $DISPLAY &
sleep 1  # wait for the server gets ready
# glxinfo | grep "OpenGL version"

# 2. start x11 and vnc connection
# to inspect logs in detail, use --verbose
x11vnc -display $DISPLAY -passwd $VNCPASS -forever -rfbport 5900 &
sleep 2  # wait for the server gets ready

# 2.5 start audio
# this is not required.
# pulseaudio --start
# sleep 2

# 3. start noVNC
/noVNC-1.1.0/utils/launch.sh --vnc localhost:5900 --listen $NOVNC_PORT &
sleep 2

# Run yuzu emulator
#/yuzu/build/bin/yuzu &

# Run yuzu REST api
#python3 /workspace/yuzulib/run_server.py --host 0.0.0.0 --port 6000 &
#python3 $API_FILE_PATH --host $API_HOST --port $API_PORT &

# bash
/bin/bash
