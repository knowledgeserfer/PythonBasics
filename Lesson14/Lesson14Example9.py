#Tuples are unchangeable, or immutable as it also is called
#You can convert the tuple into a list, change the list, 
#and convert the list back into a tuple
varCarTuple1 = ("Dodge", "Ford", "Toyota")
print(varCarTuple1)
print(type(varCarTuple1))
tempList = list(varCarTuple1)
tempList[1] = "Honda"
print(tempList)
print(type(tempList))
varCarTuple1 = tuple(tempList)
print(varCarTuple1)
print(type(varCarTuple1))

