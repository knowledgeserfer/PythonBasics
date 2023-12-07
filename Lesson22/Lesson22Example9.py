import os

try:
    os.mkdir("dir1")
    with open("dir1/file.txt","w") as fileInUse:
        fileInUse.write("Python is a solid choice")
    with open("dir1/file.txt", "r") as fileInUse:
        content = fileInUse.read()
        print(content)
        
except Exception as e:
    print(e)
    
    

    

