# from pathlib import WindowsPath, Path
# import os, shelve

# wnObj = Path('spam', 'bacon', 'eggs')

# print(Path.cwd())
# os.makedirs('c:/Users/richa/OneDrive/Documents/fgoServants') creates the fgoservants folder
# os.makedirs('c:/Users/richa/OneDrive/do/fgoServants') creates both the do folder and the fgoServants folder

# creates Path object
# print(Path.home())

# Path(r"C:\Users\richa\OneDrive\do\fgoServants").mkdir() returns error
# Path(r"C:\Users\richa\OneDrive\Documents\fgoServants").mkdir() creates fgoservants folder

# print('this is a test'.is_absolute())
# print(Path(r'C:\Users\richa\OneDrive\Documents').is_absolute())
# print(os.path.isabs(r'C:\Users\richa\OneDrive\Documents'))

# os.path.getsize(pathName)
# os.listdir(pathName)

# print(os.listdir('C://Users/richa/OneDrive/Documents'))

# path = Path.cwd()
# splitPath = os.path.split(path)
# docPath = Path(splitPath[0])
# print(list(docPath.glob('*')))

# newFile = Path(f'{docPath}/fgoServants.txt')
# newFile.write_text('Shuten Douji')
# print(newFile)
# file = open(newFile)
# file.write(' is really cute!')
# file.close()
# print(file.read())
# print(file.read())


# shelfFile = shelve.open('fgoServants.txt')
# servants = ['illya', 'kama', 'miyu']
# shelfFile['servants'] = servants
# shelfFile.close()

# print(shelfFile['servants'])
# shelfFile.close()

# import pprint

# servants = [{'name': 'miyu', 'class': 'caster'}, {'name': 'melusine', 'class': 'lancer'}]
# pprint.pformat(servants)
#sorts the above array alphabetically by key name
# fileObj = open('fileName.py', 'w')
# fileObj.write('servants = ' + pprint.pformat(servants) + '\n')
# fileObj.close()

# import fileName

# print(fileName.servants)