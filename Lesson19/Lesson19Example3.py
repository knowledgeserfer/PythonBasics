#A variable created in the main body of the Python code is a global variable 
#and belongs to the global scope.
#Global variables are available from within any scope, global and local.
car = "Dodge"

def printCar():
    print(car)
    
printCar()
print(car)
