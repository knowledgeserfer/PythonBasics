#You cannot copy a dictionary simply by typing dictionary2 = dictionary1, 
#because: dictionary2 will only be a reference to dictionary1, 
#and changes made in dictionary1 will automatically also be made in dictionary2.
#You can use copy() method or a constructor to make a copy of a dictionary.
carDictionary1 = dict(brand="Dodge", model="Charger")
carDictionary2 = carDictionary1.copy()
carDictionary3 = dict(carDictionary2)
print(carDictionary1)
print(carDictionary2)
print(carDictionary3)
carDictionary1["year"]=2020
carDictionary2["color"]="yellow"
print(carDictionary1)
print(carDictionary2)
print(carDictionary3)
