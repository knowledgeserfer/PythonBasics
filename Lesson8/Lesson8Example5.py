varList1 = ["Dodge", "Ford"]
varList2 = varList1
varList3 = ["Dodge", "Ford"]
print(varList1 is varList3) #False
print(varList1 == varList3) #True
print(varList1 is not varList3) #True
print("Check for is not False goes next")
print(varList1 is not varList2) #False
print(varList1 is varList2) #True


