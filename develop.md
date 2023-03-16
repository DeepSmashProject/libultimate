
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


# Errors

```
GUI.RenderLoop Gpu GLPERF: DebugSeverityMedium: Buffer performance warning: Buffer object 1010 (bound to GL_COPY_WRITE_BUFFER_BINDING_EXT, usage hint is GL_DYNAMIC_DRAW) is being copied/moved from VIDEO memory to HOST memory.
```



### <Error> core/memory.cpp:Write:641: Unmapped Write8 0x00000000 on Yuzu
https://github.com/yuzu-emu/yuzu/issues/6255
black screenとなっている
firmwareのバージョンを1.4.11 -> 1.6.0に変更した
Yuzuはmainline1364を使用

```
155.988911] HW.Memory <Error> core/memory.cpp:Write:641: Unmapped Write8 0x00000000 @ 0x00000000068A0018 [ 155.988912] HW.Memory <Error> core/memory.cpp:Write:641: Unmapped Write32 0x00000000 @ 0x00000000068A0014 [ 155.988913] HW.Memory <Error> core/memory.cpp:Write:641: Unmapped Write32 0x00000000 @ 0x00000000068A0010 [ 155.988914] HW.Memory <Error> core/memory.cpp:Write:641: Unmapped Write32 0x00000000 @ 0x00000000068A000C [ 155.988915] HW.Memory <Error> core/memory.cpp:Write:641: Unmapped Write32 0x00000000 @ 0x00000000068A0008 [ 155.988916] HW.Memory <Error> core/memory.cpp:Write:641: Unmapped Write32 0x00000000 @ 0x00000000068A0004 [ 155.989016] HW.Memory <Error> core/memory.cpp:Write:641: Unmapped Write32 0x00E726D4 @ 0x00000000068A0000 [ 155.989021] HW.Memory <Error> core/memory.cpp:Write:641: Unmapped Write32 0x00000000 @ 0x00000000068A0004 [ 155.989022] HW.Memory <Error> core/memory.cpp:Write:641: Unmapped Write32 0x00000000 @ 0x00000000068A0008 [ 155.989023] HW.Memory <Error> core/memory.cpp:Write:641: Unmapped Write32 0x00000000 @ 0x00000000068A000C
```

### Couldn't find selected interface None yuzu
firmwareを更新後以下のエラーが発生し、black screenとなっている

```
Couldn't find selected interface None yuzu
```

- selected interfaceはlocal通信などを行うときに必要で今は必要ないから無視して良さそう？

### yuzu mainlineを2021/12の時のに変更して行う
yuzu 850

- DELL PCの時はUnmapped Write8 0x00000000,  Couldn't find selected interfaceエラーが出ているが画面が表示されている。

#### Black screenの解決法
Restartしたら表示されるようになった！

### 現在のmainlineでできるか確認する