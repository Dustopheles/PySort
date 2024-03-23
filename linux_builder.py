"""Windows 8+ PyInstall AppBuilder."""

import os
import PyInstaller.__main__

parameter_list = [
    './kivysort/main.pyw',
    '--noconfirm',
    '--log-level=WARN',
    '--name=pysorter',
    '--noconsole'
]

PyInstaller.__main__.run(parameter_list)

SPEC = ""
with open('pysorter.spec', 'r', encoding='utf8') as file:
    SPEC = file.read()

abs_path = os.path.abspath('.')
local_path = os.path.join(abs_path, 'kivysort', '')

SPEC = SPEC.replace('exe,', rf"exe, Tree('{local_path}'),")

with open('pysorter.spec', 'w', encoding='utf8') as file:
    file.write(SPEC)

parameter_list = [
    './pysorter.spec',
    '--noconfirm',
    '--log-level=WARN',
]

PyInstaller.__main__.run(parameter_list)
