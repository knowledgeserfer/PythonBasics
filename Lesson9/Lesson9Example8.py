#You can have if statements inside if statements, 
#this is called nested if statements
#
varNum1 = 7
if varNum1>5:
    pass

if varNum1>10:
    print("varNum1 is greater than 10")
    if varNum1>20:
        print("varNum1 is greater than 20")
        if varNum1>30:
            print("varNum1 is greater than 30")
        else:
            print("varNum1 is less than or equal to 30")
            
else:
    print("varNum1 is less or equal to ten")
    
