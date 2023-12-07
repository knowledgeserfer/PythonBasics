#You can loop through a dictionary by using a for loop
carDictionary = dict(brand="Dodge", model="Charger")
print("option 1 - loop through keys")
for carkey in carDictionary:
    print(carkey)
print("option 2 - loop through values")
for carkey in carDictionary:
    print(carDictionary[carkey])
print("option 3 - use values method")
for car in carDictionary.values():
    print(car)
print("option 4 - use keys method")
for carkey in carDictionary.keys():
    print(carkey)
print("option 5 - use items method")
for carkey, car in carDictionary.items():
    print(carkey, car)
