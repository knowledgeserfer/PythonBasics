#You can define as many exception blocks as you want
#if you want to execute a special block of code for a special kind of error
#print(varNum1)
try:
    print(varNum1)
    
except NameError:
    print("Variable is not defined.")
    
except:
    print("Something went wrong.")
    


