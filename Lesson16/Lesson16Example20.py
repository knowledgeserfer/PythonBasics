#you can add several dictionaries into a new dictionary
car1 = {
    "brand": "Dodge",
    "model": "Charger"
    }
car2 = {
    "brand": "Ford",
    "model": "Mustang"
    }
carPark = {
    "car1": car1,
    "car2": car2
    }
for car in carPark:
    for carIn in carPark[car]:
        print(carPark[car][carIn])
        
