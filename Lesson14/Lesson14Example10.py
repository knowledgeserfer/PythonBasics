#tuples are immutable. In case you need to add an item to tuple
#convert it to list, make changes and convert list back to tuple
varCarTuple1 = ("Dodge", "Ford", "Toyota")
print(varCarTuple1)
tempList = list(varCarTuple1)
tempList.append("Lincoln")
varCarTuple1 = tuple(tempList)
print(varCarTuple1)
