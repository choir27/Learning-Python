import os, zipfile
from pathlib import Path

currentPath = Path.cwd()

for folderName, subFolders, fileNames in os.walk(f'{currentPath}/PythonAutomateBook'):
    print(fileNames)


newZip = zipfile.ZipFile('Test.zip', 'w')
# newZip.write('servants.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()