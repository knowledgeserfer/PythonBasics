#the variable, which is inside a function, is not available outside 
#the function, but it is available for any function inside the function
def displayCar():
    car = "Dodge"
    def printCar():
        print(car)
    printCar()
    
displayCar()
#print(car)