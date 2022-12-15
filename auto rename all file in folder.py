import os 
i = 1
path = input('Enter Path: ')
setName = input('Enter new name: ')
extension = input('Enter file extension: ')
path = path + '/'
for filename in os.listdir(path):
    file_extension = filename.split('.')
    fileex = setName + str(i) + '.' + str(extension)
    Sourcefile = path + filename
    file = path + fileex
    os.rename(Sourcefile,file)
    i += 1
print('All file was rename !')    
    