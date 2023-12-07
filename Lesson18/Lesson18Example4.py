#The finally block, if specified, will be executed regardless 
#if the try block raises an error or not.
try:
    print(varNum1)
    
except:
    print("Something went wrong.")
    
finally:
    print("End of try except.")
    
