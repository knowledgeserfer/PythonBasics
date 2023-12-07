#To determine if a specified item is present in a list 
#use the 'in' keyword
varCarList1 = ["Dodge", "Ford", "Toyota"]
checkForItem1 = "Dodge" in varCarList1
checkForAbsenceItem1 = "Dodge" not in varCarList1
print(varCarList1)
print(checkForItem1)
print(checkForAbsenceItem1)
#To change the value of a specific item, 
#refer to the index number
varCarList1[2] = "Honda"
print(varCarList1) #['Dodge', 'Ford', 'Honda']
varCarList1[0:2]=["Chrysler", "Lincoln"]
print(varCarList1) #['Chrysler', 'Lincoln', 'Honda']
varCarList1[0:2] = ["Dodge", "Ford", "Nissan"]
print(varCarList1) #['Dodge', 'Ford', 'Nissan', 'Honda']
varCarList1[0:2] = ["Chrysler"] #['Chrysler', 'Nissan', 'Honda']
print(varCarList1)

