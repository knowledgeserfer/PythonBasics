#The values() method will return a list of all the values 
#in the dictionary.
carDictionary = dict(brand="Dodge", model="Charger")
valuesExtract = carDictionary.values()
print(carDictionary)
print(valuesExtract)
#add new key=value pair
carDictionary["year"]=2020
print(carDictionary)
print(valuesExtract)

