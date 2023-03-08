
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

select OpenGL


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

```
Unhandled exception caught: System.IndexOutOfRangeException: Index was outside the bounds of the array.
at Ryujinx.Graphics.Vulkan.Window.CreateSwapChain() in 
```

DELL PC
```
install ryujinx
prodkey, firmware, game dirの設定
nvidia-xconfigでnvidia-smiが使えるようにする
memory modeをsoftwareにする
graphicsをvulkanでGeForceにする
起動(起動時環境変数はいらない)
```

System -> Enable FS Integrity Checksをオフにすると以下のエラーが発生した
```
[xcb] Unknown sequence number while processing queue
XinitThreads has not been called
```


### 研究室サーバーでもたまにできた
ただ、画面が変化しない状態
```
__GLX_VENDOR_LIBRARY_NAME=nvidia DRI_PRIME=1 ./Ryujinx
```

Settings:
```
Enable VSync: True
Enable PPTC: True
Enable Guest Internet Access: True
Enable FS Integrity Checks: True
Expand DRAM: True
Ignore Missing Services: True

Memory Manager: Software

Graphics Backend: OpenGL
Enable ShaderCache: False
Enable Texuture Recompression: False
```

### おそらくOpenGLVersionの違い
- DellのPCはホストでOpenGL4系を使用していた。
  - libultimateコンテナ内ではOpenGL3系になっていた
  - これが、開けなかった原因？
- 研究室のサーバーはホストでOpenGLバージョンを確認できなかった。
  - 
- Yuzuのときはコンテナ内でもOpenGL 4系を使用できたはず？
  - YuzuがXOrg系のエラーで起動しない
  - エラー：The directory "/usr/share/fonts/X11/100dpi" does not exist.
    - sudo apt-get install xfonts-base


CommitID: 22593ad63f4c68d6af17c5f99afc45357215a299

- prime-runを行うとOpenGL 4.6となった！！
https://askubuntu.com/questions/1364762/prime-run-command-not-found
export __NV_PRIME_RENDER_OFFLOAD=1
export __GLX_VENDOR_LIBRARY_NAME=nvidia
export __VK_LAYER_NV_optimus=NVIDIA_only

```
__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia __VK_LAYER_NV_optimus=NVIDIA_only glxinfo | grep "OpenGL version"
```

- ただ、数回に一回しかversionが出ず、他の時は以下のエラーが発生する
```
name of display: :1
```


### XServerが起動していないためNvidiaのGPU Screenを使えていない

```
[2400788.252] (EE) NVIDIA(GPU-0): Failed to acquire modesetting permission.
[2400788.252] (EE) NVIDIA(0): Failing initialization of X screen
```
Xorgのこのエラーを治したい


### 2023/03追記

```
__GLX_VENDOR_LIBRARY_NAME=nvidia glxinfo | grep "OpenGL version"
```
のみでOpenGL versionが4系となった
```
__GLX_VENDOR_LIBRARY_NAME=nvidia /home/default/.local/share/Ryujinx/Ryujinx
```

- Valkanの場合
```
GUI.RenderLoop Application System.IndexOutOfRangeException
```
- OpenGLの場合
```
SPB.Graphics.Exception.ContextException: MakeCurrent() failed.
```

2. __VK_LAYER_NV_optimus=NVIDIA_onlyを加える
```
__GLX_VENDOR_LIBRARY_NAME=nvidia __VK_LAYER_NV_optimus=NVIDIA_only /home/default/.local/share/Ryujinx/Ryujinx
```

OpenGLで初めて起動できた。ゲームも正常に動く
- ただ最初の一回のみで、次以降はFPSは回っているが、画面が開かなかった
- その後、__VK_LAYER_NV_optimus=NVIDIA_onlyなしでも一度動いた

Settings:
- System:  Memory Manager Mode: Software

Vulkan Quadro,nvidiaの場合変わらず同じエラーが発生した。
```
GUI.RenderLoop Application System.IndexOutOfRangeException
```