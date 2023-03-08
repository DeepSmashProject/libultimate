# libultimate

Open API written in Python 3 for making your own Smash Bros Ultimate AI that works with RyujinX

## Get Started with docker

1. docker/.env.tmplateをdocker/.envに変更し内容を編集します。
```
NOVNC_PORT=8081
GAME_DIR=
FIRMWARE_DIR=
PRODKEYS_DIR=
NVIDIA_DRIVER_VERSION=
VNC_PASSWORD=pass
```

2. docker buildを行う

```
make build
```

3. docker runを行う

```
make run
```

後始末は以下のコマンドでできます。
```
make remove
```

4. ターミナルを開いてRyujinxを起動する

```
$HOME/.local/share/Ryujinx/Ryujinx
```
最初にprod.keysがないことを言われるがとりあえず起動します。
起動によって$HOME/.config/Ryujinxフォルダが作成されます。

ValkanかOpenGLのどちらを使うか聞かれるのでOpenGLを選択します。

5. prod.keysをコピーし、Ryujinxを再起動する

```
cp $HOME/data/keys/prod.keys $HOME/.config/Ryujinx/system/prod.keys
```

再起動する際は以下のコマンドで再起動します。
```
__GLX_VENDOR_LIBRARY_NAME=nvidia __VK_LAYER_NV_optimus=NVIDIA_only $HOME/.local/share/Ryujinx/Ryujinx
```

6. firmwareとgameを設定する
Tools->InstallFirmware->Install from Zipを選択し、$HOME/data/firmware/xxx.zipを選択する
Options->Settings->General->Addから$Home/data/games/SSBU(nspのあるフォルダ)を選択する

7. Settingsを変更する
最速にするには
- Logging->Log出力をなくす
- System -> MemoryManagerMode -> Host Uncheckedにする
- Graphics -> Resolution Scaleで低画質にする
- System -> Enable xxxのチェックを外す？？
   - Enable VSyncを外すと60fpsの制限がなくなりframeが早くなる
などを試してください。

8. ゲームを起動する

### Skyline Pluginを使用する

9. DLCを導入する
libparam-hook.nroが13.0.1対応なので13.0.1にアップデートしないといけない
Ryujinxのゲームタイトルを右クリックし、Manage DLC->v13.0.1のnspを選択する

10. pluginを導入する
release/contentsを$HOME/.config/Ryujinx/mods/contentsに入れる
```
cp -r release/contents/01006A800016E000 $HOME/.config/Ryujinx/mods/contents
```

11. (option) skyline listenでpluginのログをチェックする

skylineをインストールする
```
cargo install cargo-skyline
```

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

ゲームが正常に起動できれば成功です。

12. libultimateを動かす
```
cd examples
python3 basic.py
```


# Development

```
cd libultimate-plugin
cargo skyline update
cargo skyline install
cargo skyline build
```

パッケージbuild
```
make skyline-build
```