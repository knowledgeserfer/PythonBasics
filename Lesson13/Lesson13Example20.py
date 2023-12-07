#You cannot copy a list simply by typing list2 = list1, 
#because: list2 will only be a reference to list1, and 
#changes made in list1 will automatically also be made in list2.
#use the built-in List method copy()
varCarList1=["Dodge", "Ford", "Toyota"]
varCarList2=varCarList1.copy()
print(varCarList1)
print(varCarList2)
varCarList1.append("Honda")
varCarList2.append("BMW")
print(varCarList1)
print(varCarList2)

varCarList3=list(varCarList1)
print(varCarList3)
varCarList3.append("Alfa Romeo")
print(varCarList3)




