
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
