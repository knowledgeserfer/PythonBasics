#If you operate with the same variable name inside and outside of a function, 
#Python will treat them as two separate variables
car = "Dodge"

def displayCar():
    car = "Lincoln"
    print(car)
    
displayCar()
print(car)
