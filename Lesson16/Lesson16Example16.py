#del keyword can remove the item with the specified key name
#del keyword can also delete the dictionary completely
#clear() method empties the dictionary
carDictionary = dict(brand="Car", model="Some model", year=2000)
print(carDictionary)
del carDictionary["year"]
print(carDictionary)
carDictionary.clear()
print(carDictionary)
del carDictionary
#print(carDictionary)
