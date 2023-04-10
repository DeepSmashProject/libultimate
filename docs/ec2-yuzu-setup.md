# Setup libultimate with yuzu emulator on EC2

## 1. Create Instance

- instance: g4dn.xlarge
- OS: Ubuntu 20.04
- ssd: 30GB

## 2. Setting Inbound Rule
EC2->Instance->YourInstance->Security
Move to security group settings.

Add Inbound Rule
- Type: Custom TCP
- Port: 6080
- Source: 0.0.0.0/0 or Your device ip

## 3. Install nvidia

```
ssh -i "~/.ssh/your_pem.pem" ubuntu@[EC2_DNS_NAME]
```

### Install common packages
```
sudo apt update \
    && sudo apt install -y --no-install-recommends \
    curl \
    wget \
    vim \
    zip \
    unzip \
    git \
    mesa-utils
```

### Install nvidia driver
Yuzu required nvidia-driver-440

```
sudo apt-get install nvidia-driver-440
sudo modprobe nvidia
```

Check nvidia version
```
nvidia-smi
```

## 4. Install Xfce

```
sudo apt-get install -y xfce4 xfce4-terminal xterm
```
select 'dgm3' on installation.

```
mkdir -p $HOME/.vnc
vim ~/.vnc/xstartup
```

```
#!/bin/sh

unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
startxfce4 &
```

## 5. Install and Run VNC

```
sudo apt-get install tigervnc-standalone-server tigervnc-xorg-extension tigervnc-viewer
```

Run VNC server.
```
/usr/bin/vncserver :1 -geometry 1366x768 -depth 24
```

(Option): If you want to kill vnc server, run below command.
```
/usr/bin/vncserver -kill :1
```

## 6. Install and Run noVNC
```
sudo apt install -y \
    net-tools \
    novnc \
    && sudo ln -s /usr/share/novnc/vnc_lite.html /usr/share/novnc/index.html
```

Run noVNC server
```
/usr/share/novnc/utils/launch.sh --vnc localhost:5901 --listen 6080 &
```

## 7. Install Yuzu Emulator
Please change the version accordingly.
Reference: https://github.com/yuzu-emu/yuzu-mainline/releases

```
sudo apt-get install -y xdg-utils
 wget https://github.com/yuzu-emu/yuzu-mainline/releases/download/mainline-0-1364/yuzu-mainline-20230308-9e9548d12.AppImage \
    && chmod a+x yuzu-mainline-20230308-9e9548d12.AppImage \
    && ./yuzu-mainline-20230308-9e9548d12.AppImage --appimage-extract \
    && chmod a+x squashfs-root/AppRun && mkdir yuzu-mainline && mv squashfs-root/* yuzu-mainline
```

## 8. Create EFS
Move to AWS EFS Console.

### Add Inbound Role for mount
- Type: CustomTCP
- Port: 2049
- Source: YOUR_EC2_SECURITY_GROUP, ex. sg-xxxxxxxxxx

### Mount EFS on EC2 Instance
on EC2 terminal.

```
sudo apt-get install -y nfs-common
sudo apt-get -y install git binutils
git clone https://github.com/aws/efs-utils
cd efs-utils
./build-deb.sh
sudo apt-get -y install ./build/amazon-efs-utils*deb

sudo mkdir /mnt/efs
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-xxxxxxxxxxxx.efs.ap-northeast-1.amazonaws.com:/ /mnt/efs
```

## 9. Download Game Files
Recommend for using scp command.

### Example
on EC2 instance.
```
mkdir -p /mnt/efs/game
sudo chmod 777 /mnt/efs/game  // allow permission
```

on your computer
```
scp -i "~/.ssh/YOUR_PEM.pem" ~/YOUR_PATH/SuperSmashBrosUltimate_v0.nsp [USER_NAME]@[DNS_NAME]:/mnt/efs/game/SuperSmashBrosUltimate_v0.nsp
```

Copy firmware and prod.keys by same way.

## 10. Make sure the game works in Yuzu
on EC2 instance.

```
~/yuzu-mainline/AppRun
```

You can xcfe desktop on browser at http://[EC2_PUBLIC_IP]:6080.
Run ssbu.

## 11. Install libultimate
### Important!
Please update your SSBU title to 13.0.1, as libultimate is only compatible with 13.0.1

### Install libultimate plugin.
```
export LIB_ULTIMATE_VERSION=1.2.1

mkdir $HOME/data && \
curl -L https://github.com/DeepSmashProject/libultimate/releases/download/${LIB_ULTIMATE_VERSION}/release.zip > $HOME/data/release.zip && \
unzip $HOME/data/release.zip -d $HOME/data && rm $HOME/data/release.zip
```

Move plugin to yuzu atmosphere path. 
```
cp -r ~/data/release/contents/01006A800016E000/* ~/.local/share/yuzu/sdmc/atmosphere/contents/01006A800016E000/
```

Restart SSBU.

### Install libultimate library
```
sudo apt-get install -y python3 python3-pip
sudo pip install git+https://github.com/DeepSmashProject/libultimate.git@$LIB_ULTIMATE_VERSION
```

## 12. (Option) Run API Server

Add inbound role on EC2 security group
- Type: Custom TCP
- Port: 8008
- Source: 0.0.0.0/0 or Your device ip

```
git clone https://github.com/DeepSmashProject/libultimate.git -b $LIB_ULTIMATE_VERSION
cd libultimate/examples
```

Change SDCARD_PATH to ~/.local/share/yuzu/sdmc on server.py.
```
python3 server.py
```

View swagger ui at http://[EC2_PUBLIC_IP]:8008/docs

### Run API Client on your local computer

Change SERVER_ADDRESS to http://[EC2_PUBLIC_IP]:8008 on client.py.
```
cd libultimate/examples
python3 client.py
```

redirect 80 to 8080
```
sudo iptables -t nat -L
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 8080
```