import os

os.rename("dir1/file.txt", "dir1/fileRenamed.txt")
with open("dir1/fileRenamed.txt", "r") as fileInUse:
    content = fileInUse.read()
    print(content)

