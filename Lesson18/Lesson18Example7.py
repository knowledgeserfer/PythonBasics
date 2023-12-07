#Python 3.6 uses the input() method.
#Python 2.7 uses the raw_input() method.
#Python stops executing when it comes to the input() function, 
#and continues when the user has given some input.
varNum1 = float(input("Enter number 1: "))
varNum2 = float(input("Enter number 2: "))

try:
    divisionResult=varNum1/varNum2
    print("{} divided by {} equals {}".format(varNum1,varNum2,divisionResult))
except ZeroDivisionError:
    print("You can not divide by zero.")
    
    

    


