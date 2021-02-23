from pathlib import Path
cwd = Path.cwd()
demo_file = Path(Path.joinpath(cwd, 'demo.txt'))

print('File name: ' + demo_file.name)
print('File suffix: ' + demo_file.suffix)
print('File Folder: ' + demo_file.parent.name)
print('File size: ' + str(demo_file.stat().st_size))
