#Recursion is a common mathematical and programming concept. 
#It means that a function calls itself. 
#This has the benefit of meaning that you can loop through data 
#to reach a result.
def recursion_function(num1):
    if(num1<10):
        result=0
        print(num1)
        print(result)
        result = num1 + recursion_function(num1+1)
        print(result)
    else:
        result=10
        print("Else statement works.")
    return result

recursion_function(1)
        
