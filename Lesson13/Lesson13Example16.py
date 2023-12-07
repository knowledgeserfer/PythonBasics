#newlist = [expression for item in iterable if condition == True]
#The return value is a new list, leaving the old list unchanged.
varCarList1 = ["Dodge", "Ford", "Toyota"]
varCarList2 = []
for car in varCarList1:
    varCarList2.append(car)    
print("varCarList 1 {}".format(varCarList1))
print("varCarList 2 {}".format(varCarList2))
varCarList3 = [car for car in varCarList1]
print("varCarList 3 {}".format(varCarList3))
#print elements of the list with comprehension syntax
[print(car) for car in varCarList3]
