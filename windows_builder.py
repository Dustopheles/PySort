"""Windows 8+ PyInstall AppBuilder."""

import os
import PyInstaller.__main__

parameter_list = [
    '.\\kivysort\\main.pyw',
    '--noconfirm',
    '--log-level=WARN',
    '--name=pysorter',
    '--noconsole'
]

PyInstaller.__main__.run(parameter_list)

SPEC = ""
with open('pysorter.spec', 'r', encoding='utf8') as file:
    SPEC = file.read()

SPEC = 'from kivy_deps import sdl2, glew\n' + SPEC

abs_path = os.path.abspath('.')
local_path = os.path.join(abs_path, 'kivysort', '')
local_path = local_path.replace('\\', '\\\\')

SPEC = SPEC.replace('a.datas,', "a.datas, *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],")
SPEC = SPEC.replace('exe,', rf"exe, Tree('{local_path}'),")

with open('pysorter.spec', 'w', encoding='utf8') as file:
    file.write(SPEC)

parameter_list = [
    '.\\pysorter.spec',
    '--noconfirm',
    '--log-level=WARN',
]

PyInstaller.__main__.run(parameter_list)
