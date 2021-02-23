from pathlib import Path

cwd = Path.cwd()
print('Current directory: \n' + str(cwd))

new_file = Path.joinpath(cwd, 'new_file.txt')
print('Does that file exist? ' + str(new_file.exists()))
