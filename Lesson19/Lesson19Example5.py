#The global keyword makes the variable global.
car = "Dodge"

def displayCar():
    global car
    car = "Lincoln"
    print(car)

print(car)    
displayCar()
print(car)
