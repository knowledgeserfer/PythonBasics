#update() method will update the dictionary with the items 
#from a given argument. 
#If the item does not exist, the item will be added.
#The argument must be a dictionary, or an iterable object 
#with key:value pairs.
carDictionary = dict(brand="Dodge", model="Charger")
print(carDictionary)
carDictionary.update({"model":"Challenger"})
carDictionary.update({"year":2020})
print(carDictionary)


