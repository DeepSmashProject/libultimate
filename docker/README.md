
# Docker for Ryujinx and libultimate

## Config Setting

## Run Docker Image

```
bash run.sh
```

## Run Ryujinx

```
# /install_ryujinx.sh
cd /
/home/guest/.local/share/Ryujinx/Ryujinx
```


- move prod.keys
to /root/.config/Ryujinx/system/
```
cp /data/keys/prod.keys /root/.config/Ryujinx/system/prod.keys
```
- install firmware
  - select /data/firmware/Firmware.14.1.2.zip
- add game
  - options -> game add -> select /data/games
- title update
  - select /data/games/DLC/13.0.1.nsp

# Errors

 System.ComponentModel.Win32Exception (2): An error occurred trying to start process '/home/guest/.local/share/Ryujinx/Logs' with working directory '/'. No such file or directory
/home/guest/.local/share/Ryujinx/Logs

System.ComponentModel.Win32Exception (2): An error occurred trying to start process '/root/.config/Ryujinx' with working directory '/'. No such file or directory

/root/.config/Ryujinx
Win32Exception No such file or directory


# memo 
https://own-search-and-study.xyz/2020/05/02/docker-container-ubuntu-desktop-rdp/

https://kokensha.xyz/docker/access-headless-docker-linux-desktop-container-via-vnc/
# Docker 対応

docker run -p 6080:80 -p 5900:5900 -v /dev/shm:/dev/shm dorowu/ubuntu-desktop-lxde-vnc
ではRyujinxを起動でき、Logも表示できた

Github: https://github.com/fcwu/docker-ubuntu-vnc-desktop

```
apt install -y libx11-dev libsdl2-dev firefox tar
firefox -> downloa Ryujinx
tar -xzvf xxx.tar.gz
chmod a+x Ryujinx
./Ryujinx
```
が必要

### https://github.com/RavenKyu/docker-ubuntu-desktop-vnc

これであれば、ubuntu desktopで実行できる。


### error
settingでLogを全て出すようにしたら以下のエラーが発生していた
Memory Manage Mode = softwareにするとエラーが見れる

```
Application: Unhandled exception caught:SPB.
Graphics.Exceptions.ContextException: CreateContext() failed.
at SPB.Platform.GLX.GLXOpenGLContext.Initialize
```

https://github.com/Ryujinx/Ryujinx/issues/2220
https://github.com/Ryujinx/Ryujinx/issues/2112

```
__GLX_VENDOR_LIBRARY_NAME=nvidia DRI_PRIME=1 ./Ryujinx
```
これにより2回に1回くらいできるようになった
(nvidia-xconfigしてnvidia-smiができるようになった状態で)


```
apt install libx11-dev libsdl2-dev
```

bash -c "$(curl -s https://raw.githubusercontent.com/edisionnano/Pine-jinx/main/pinejinx.sh)"

### 研究室サーバだとできない問題

Vulkanを使用するといいっぽい。

研究室サーバーはnvidia 460だからvulkanに対応してない？
- settingでvulkanにするとllvmpipeのおそらく初期GPUっぽいものしかない
- dellだとGeForceがでてくる
- nvidia driver 470以降？


DELLではvulkanでできたが、研究室サーバーだと以下のエラーが発生
DELL PC
```
install ryujinx
prodkey, firmware, game dirの設定
nvidia-xconfigでnvidia-smiが使えるようにする
memory modeをsoftwareにする
graphicsをvulkanでGeForceにする
起動(起動時環境変数はいらない)
```
