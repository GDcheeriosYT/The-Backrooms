import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '-n The-Backrooms',
    '-c',
    '--collect-all panda3d',
    '--collect-all ursina'
])
