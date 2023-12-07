#items() method will return each item in a dictionary, 
#as tuples in a list
carDictionary=dict(brand="Dodge", model="Charger")
itemsExtract = carDictionary.items()
print(carDictionary)
print(itemsExtract)
#add new key=value pair
carDictionary["year"]=2020
print(carDictionary)
print(itemsExtract)
