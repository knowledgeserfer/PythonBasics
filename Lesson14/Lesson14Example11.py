#Tuples are unchangeable, so you cannot remove items from it
#The workaround is the same, convert tuple to list, make changes,
#and convert list back to tuple
varCarTuple1 = ("Dodge", "Ford", "Toyota", "Car1")
print(varCarTuple1)
tempList = list(varCarTuple1)
tempList.pop()
varCarTuple1 = tuple(tempList)
print(varCarTuple1)

