
   
# inside docker script
trap 'kill $(jobs -p)' EXIT

# 0. generate xorg.conf
# This is for OpenGL 4.6.0
BUS_ID=$(nvidia-xconfig --query-gpu-info | grep 'PCI BusID' -m 1 | sed -r 's/\s*PCI BusID : PCI:(.*)/\1/')
echo "BUS_ID=$BUS_ID"
sudo nvidia-xconfig -a --virtual=$RESOLUTION --allow-empty-initial-configuration --enable-all-gpus --busid $BUS_ID

# bash
/bin/bash
