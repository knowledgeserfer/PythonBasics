#The symmetric_difference_update() method will keep only 
#the elements that are NOT present in both sets
varCarSet1 = {"Dodge", "Ford", "Toyota"}
varCarSet2 = {"Dodge", "Honda", "Lincoln"}
print(varCarSet1)
print(varCarSet2)
varCarSet1.symmetric_difference_update(varCarSet2)
print(varCarSet1)
print(varCarSet2)
