import PyInstaller.__main__

parameter_list = [
    '.\\kivysort\\main.pyw',
    '--noconfirm',
    '--log-level=WARN',
    '--name=pysorter',
    '--icon=.\\kivysort\\res\\nxLogo.ico',
    '--noconsole'
]

PyInstaller.__main__.run(parameter_list)

spec = ""
with open('pysorter.spec', 'r', encoding='utf8') as file:
    spec = file.read()

spec = 'from kivy_deps import sdl2, glew\n' + spec

spec = spec.replace('a.datas,', "a.datas, *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],")
spec = spec.replace('exe,', r"exe, Tree('C:\\Projekte\\PySort\\kivysort\\'),")

with open('pysorter.spec', 'w', encoding='utf8') as file:
    file.write(spec)

parameter_list = [
    '.\\pysorter.spec',
    '--noconfirm',
    '--log-level=WARN',
]

PyInstaller.__main__.run(parameter_list)
