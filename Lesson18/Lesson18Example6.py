#You can define what kind of error to raise, and the text 
#to print to the user.
varNum = "Text"

if not type(varNum) is int:
    raise TypeError("Invalid type. Only integers can be accepted.")

else:
    print(varNum)


