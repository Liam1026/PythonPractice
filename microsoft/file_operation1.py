from pathlib import Path
cwd = Path.cwd()
print(cwd)
parent = cwd.parent
print('Is this a directory? ' + str(parent.is_dir()))
print('Is this a file? ' + str(parent.is_file()))

print('---Directory contents---')
for child in parent.iterdir():
    if child.is_dir():
        print(child)
