#pop() method removes the item with the specified key name
#popitem() method removes the last inserted item 
#(in versions before 3.7, a random item is removed instead)
carDictionary=dict(brand="Car", model="Some model", year=2000)
print(carDictionary)
carDictionary.pop("year")
print(carDictionary)
carDictionary.popitem()
print(carDictionary)