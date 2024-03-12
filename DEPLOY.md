# Deploy project with PyInstaller

```
pyinstaller --name sorter --icon .\kivysort\res\nxLogo.ico --noconsole .\kivysort\main.pyw
pyinstaller .\sorter.spec 
```


```
from kivy_deps import sdl2, glew
# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['kivysort\\main.pyw'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='sorter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['kivysort\\res\\nxLogo.ico'],
)
coll = COLLECT(
    exe, Tree('C:\\Projekte\\PySort\\kivysort\\'),
    a.binaries,
    a.datas,
    strip=False,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    upx=True,
    upx_exclude=[],
    name='sorter',
)
```