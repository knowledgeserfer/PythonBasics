#The object in the update() method does not have to be a set, 
#it can be any iterable object
varCarSet1 = {"Dodge", "Ford", "Toyota"}
varCarList1 = ["BMW", "Lincoln"]
print(varCarSet1)
print(varCarList1)
varCarSet1.update(varCarList1)
print(varCarSet1)
print(varCarList1)

