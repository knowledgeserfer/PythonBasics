#You can access the items of a dictionary by referring to 
#its key name, inside square brackets
#There is also a method called get() that will give you 
#the same result
carDictionary = dict(brand="Dodge", model="Charger")
brandExtract = carDictionary["brand"]
modelExtract = carDictionary.get("model")
print(carDictionary)
print(brandExtract)
print(modelExtract)

