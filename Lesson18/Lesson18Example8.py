#Python stops executing when it comes to the input() function, 
#and continues when the user has given some input.

try:
    varNum1 = float(input("Enter number 1: "))
    varNum2 = float(input("Enter number 2: "))
    divisionResult=varNum1/varNum2
    print("{} divided by {} equals {}".format(varNum1,varNum2,divisionResult))
except ZeroDivisionError:
    print("You can not divide by zero.")
    
except ValueError:
    print("Invalid data type. Numbers must be entered.")
    

    


