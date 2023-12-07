#By default the sort() method is case sensitive, resulting in 
#all capital letters being sorted before lower case letters
itemsList1= ["notebook", "Pencil", "flash drive", "Scissors"]
itemsList1.sort()
print(itemsList1)

itemsList1.sort(key=str.lower)
print(itemsList1)
#The reverse() method reverses the current sorting order 
#of the elements
itemsList1.reverse()
print(itemsList1)

