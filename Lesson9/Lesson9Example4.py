#if you have only one statement to execute, 
#you can put it on the same line
varNum1=85
varNum2=95
print("shorthand versions")
if varNum1<varNum2: print("varNum1 is less than varNum2")
#same for if else combination, but statement goes first
x=95
y=85
print("y greater") if y>x else print("y is not greater")
#it works alse for multiple condition
print("y") if y>x else print("equals") if y==x else print("x")

#full version
print("full version")
if y>x:
    print("y")
    
else:
    if y==x:
        print("equals")
    else:
        print("x")
        




