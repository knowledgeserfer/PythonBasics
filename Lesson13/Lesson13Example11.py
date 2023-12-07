#pop() method removes the specified index
varCarList1 = ["Dodge", "Ford", "Toyota"]
print(varCarList1)
varCarList1.pop(1)
print(varCarList1)
#If you do not specify the index, 
#pop() method removes the last item
varCarList1.pop()
print(varCarList1)
#del keyword also removes the specified index
varCarList2 = ["Chrysler", "Honda", "Lincoln"]
print(varCarList2)
del varCarList2[0]
print(varCarList2)
del varCarList2
#print(varCarList2)
# varCarList2 = ["Chrysler", "Honda", "Lincoln"]
# print(varCarList2)
