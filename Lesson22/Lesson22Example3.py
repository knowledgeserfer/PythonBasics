#with expression can be used. It closes files anyway.
# with open(filename, mode) as file_obj:
#    commands
#with expression defines a variable file_obj for opened file.
with open("file3.txt", "w") as fileInUse:
    fileInUse.write("Python is a solid choice. File3.")
    

