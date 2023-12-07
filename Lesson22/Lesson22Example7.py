#readlines() method can be used to read all the lines of the file
#they will be saved as a list
with open("file4.txt", "r") as fileInUse:
    fileContent = fileInUse.readlines()
    print(fileContent)
    
#in case there are problems with encoding you can use encoding parameter
with open("file4.txt", encoding="utf8") as fileInUse:
    fileContent = fileInUse.read()
    print(fileContent)
    

