with open("file4.txt", "r") as fileInUse:
    fileLine = fileInUse.readline()
    while fileLine:
        print(fileLine, end="")
        fileLine = fileInUse.readline()
print()
#for small files you can use read() method
with open("file4.txt", "r") as fileInUse:
    fileContent = fileInUse.read()
    print(fileContent)
    
