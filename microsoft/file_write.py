stream = open('Output.txt', 'wt')
print('Can I write to this file? ' + str(stream.writable()))

stream.write('H')
stream.writelines(['ello', ' ', 'World.'])
stream.write('\n')

names = ['Susan', 'Christopher']
stream.writelines(names)
stream.write('\n')

stream.writelines('\n'.join(names))
stream.close()