#you can read text file using cycle for
with open("file4.txt", "r") as fileInUse:
    for line in fileInUse:
        print(line, end="")#readline is used behind the scene

print("\nExplicit use of readline\n")        
with open("file4.txt", "r") as fileInUse:
    str1=fileInUse.readline()
    print(str1, end="")
    str2=fileInUse.readline()
    print(str2, end="")
    str3=fileInUse.readline()
    print(str3, end="")
    


