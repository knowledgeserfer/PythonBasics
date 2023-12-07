#You can use discard method to remove an item
#If the item to remove does not exist, 
#discard() will NOT raise an error
varCarSet = {"Dodge", "Ford", "Toyota", "Car1"}
print(varCarSet)
varCarSet.discard("Car1")
print(varCarSet)
varCarSet.discard("Car1")
print(varCarSet)
