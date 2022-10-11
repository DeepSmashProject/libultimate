docker run --privileged --gpus all --rm -it -p 8081:8081 -e NOVNC_PORT=8081 -e RESOLUTION=1280x800 -e BUS_ID=13:0:0 -e DISPLAY=:0 -e VNCPASS=pass -e DRIVER_VERSION=460.91.03 nvidia/cudagl:11.4.2-runtime-ubuntu20.04 bash

export DEBIAN_FRONTEND=noninteractive

# apt updateのためにKeyを取得
apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub

# 必要なパッケージをインストール
apt update
apt install -y sudo curl wget kmod git

# nvidia driverの前にxinitをインストール for Xorg
apt install -y xinit # timezoneを聞かれる

# nvidia driverをインストール
cd /tmp && \
curl -fSsl -O https://us.download.nvidia.com/tesla/$DRIVER_VERSION/NVIDIA-Linux-x86_64-$DRIVER_VERSION.run && \
sh NVIDIA-Linux-x86_64-$DRIVER_VERSION.run -x && \
cd NVIDIA-Linux-x86_64-$DRIVER_VERSION

./nvidia-installer --silent \
    --no-kernel-module \
    --install-compat32-libs \
    --no-nouveau-check \
    --no-nvidia-modprobe \
    --no-rpms \
    --no-backup \
    --no-check-for-alternate-installs \
    --no-libglx-indirect \
    --no-install-libglvnd

# sudo: nvidia-xconfig: command not found
#$ sudo nvidia-xconfig -a --virtual=$RESOLUTION --allow-empty-initial-configuration --enable-all-gpus --busid $BUS_ID
#sh: 1: pkg-config: not found

apt install -y --no-install-recommends pkg-config mesa-utils x11vnc x11-apps


# run nvidia xconfig (OK)
sudo nvidia-xconfig -a --virtual=$RESOLUTION --allow-empty-initial-configuration --enable-all-gpus --busid $BUS_ID

# for Xorg
#apt install -y xinit

# run xorg (OK)
sudo Xorg $DISPLAY &
# (EE) parse_vt_settings: Cannot open /dev/tty0 (No such file or directory)
# --previledgedをつけると解決する

# run x11vnc (OK)
x11vnc -display $DISPLAY -passwd $VNCPASS -forever -rfbport 5900 &

# install novnc
#wget https://github.com/novnc/noVNC/archive/v1.1.0.zip && \
#    unzip -q v1.1.0.zip && \
#    rm -rf v1.1.0.zip && \
#    git clone https://github.com/novnc/websockify /noVNC-1.1.0/utils/websockify

apt install -y novnc websockify 
/usr/bin/websockify -D --web=/usr/share/novnc/ $NOVNC_PORT localhost:5900
