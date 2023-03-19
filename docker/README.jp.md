# libultimate on Docker

Open API written in Python 3 for making your own Smash Bros Ultimate AI that works with Yuzu

# Get Started with Yuzu in docker
現状、動作確認ができているのはYuzu(OpenGL)のみです。

## 1. docker/.env.tmplateをdocker/.envに変更し内容を編集します。
```
NOVNC_PORT=8081
GAME_DIR=
FIRMWARE_DIR=
PRODKEYS_DIR=
NVIDIA_DRIVER_VERSION=
VNC_PASSWORD=pass
```

GAME_DIR: ゲームファイル(.nsp)およびDLCのデータがあるディレクトリを指定します。~/data/gamesにマウントされます。
FIRMWARE_DIR: ファームウェアのあるディレクトリを指定します。~/data/firmwareにマウントされます。
PRODKEYS_DIR: prod.keysのあるディレクトリを指定します。~/data/keysにマウントされます。

## 2. docker buildを行う
libultimateのルートディレクトリで以下のコマンドを実行する

```
make build
```

## 3. docker runを行う
libultimateのルートディレクトリで以下のコマンドを実行する

```
make run
```

後始末は以下のコマンドでできます。
```
make remove
```

localhost:{NOVNC_PORT}でubuntuを見ることができます。
NOVNC_PORTはdocker/.envに書いたものです。
VNC_PASSでログインできます。

## 4. Yuzuを起動する
localhost:8082のUbuntu Desktopでターミナルを開きます。
デフォルトがdashなのでbashに移動後Yuzuを起動します。
```
$ bash
$ ~/yuzu-mainline/AppRun
```

## 5. prod.keys, firmware, Gameを設定する
- prod.keysを導入する
File -> Open yuzu folderから
$HOME/.local/share/yuzu/keysにprod.keysをコピーする

もしくは以下のコマンドを実行

```
cp $HOME/data/keys/prod.keys $HOME/.local/share/yuzu/keys/prod.keys
```

- firmwareを導入する
$HOME/.local/share/yuzu/nand/system/Contents/registeredにfirmware.zipを解凍したファイル群をコピーする
もしくは以下のコマンドを実行

```
cd $HOME/data/firmware
unzip -d firmware Firmware.xx.x.x.zip
cp $HOME/data/firmware/firmware/* $HOME/.local/share/yuzu/nand/system/Contents/registered
```

- ゲームを設定する
Add New Game Directoryからゲームのディレクトリを選択

## 6. ゲームを起動する
Configure->GPU->OpenGL [GLSL]に変更する

その後起動する
```
~/yuzu-mainline/AppRun
```

## 7. Skyline Pluginを使用する

7. DLCを導入する
libparam-hook.nroが13.0.1対応なので13.0.1にアップデートしないといけない
File->Install Files to Nand->v13.0.1のnspを選択する

## 8. pluginを導入する
$HOME/data/release/contentsを$HOME/.local/share/yuzu/sdmc/atmosphere/contentsに入れる
```
cp -r $HOME/data/release/contents/01006A800016E000 $HOME/.local/share/yuzu/sdmc/atmosphere/contents
```

## 9. (option) skyline listenでpluginのログをチェックする

PCのipアドレスを確認する
```
hostname -I
192.168.xx.xx ....
```

listenする
```
cargo skyline set-ip 192.168.xx.xx
cargo skyline listen
```
ゲーム起動後ログが流れると思います。

# Trouble Shooting

## 1. Vulkanで起動時にoutdated GPU driversエラーが発生する
```
yuzu has encountered an error while running the video core. ...
```
Vulkanは対応していないのでOpenGL[GLSL]に変更


## 2. OpenGLで起動時にnot supportedエラーが発生する
```
OpenGL not available!
OpenGL shared contexts are not supported.
```
何回も「OK」からゲームタイトルクリックもしくはyuzu emulator自体の起動し直しを繰り返せばたまに成功する

## 3. 起動後black screenになる
Restartをするとうまく表示される時があります。
mainline-850(skyline対応なし)ではうまく表示された。
かなり運ゲーだがRestartを何回も試してmainline-1000でも表示できた。

根気強く試してください。。。

```
GUI.RenderLoop Gpu GLPERF: DebugSeverityMedium: Buffer performance warning: Buffer object 1010 (bound to GL_COPY_WRITE_BUFFER_BINDING_EXT, usage hint is GL_DYNAMIC_DRAW) is being copied/moved from VIDEO memory to HOST memory.
```