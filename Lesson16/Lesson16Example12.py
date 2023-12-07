#To determine if a specified key is present in a dictionary 
#use the in keyword
carDictionary = {
    "brand": "Dodge",
    "model": "Charger",
    "year": 2020
    }
print(carDictionary)
if "brand" in carDictionary:
    print("Key 'brand' is present in dictionary")
    
else:
    print("Key 'brand' is not present in dictionary")
