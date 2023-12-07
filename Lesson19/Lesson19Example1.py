#A variable is only available from inside the region it is created. 
#This is called scope.
#A variable created inside a function belongs to the local scope 
#of that function, and can only be used inside that function.
def displayCar():
    car = "Dodge"
    print(car)
    
displayCar()
#print(car)


