#create a new file and write some text in it.
with open("file4.txt", "w") as fileInUse:
    fileInUse.write("Java is a solid choice. File4")
    
with open("file4.txt", "w") as fileInUse:
    fileInUse.write("Python is a solid choice. File4.")
    
with open("file4.txt", "a") as fileInUse:
    fileInUse.write("\nJava is a solid choice. File4")
    
with open("file4.txt", "a") as fileInUse:
    print("\nC# is a solid choice. File4", file=fileInUse)


