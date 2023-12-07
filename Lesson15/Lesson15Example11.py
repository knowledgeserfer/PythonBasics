#You can also use the pop() method to remove an item, 
#but this method will remove a random item, 
#so you cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item.
varCarSet = {"Car1", "Car2", "Car3"}
print(varCarSet)
removedItem = varCarSet.pop()
print(varCarSet)
print("Removed item  is {}".format(removedItem))


