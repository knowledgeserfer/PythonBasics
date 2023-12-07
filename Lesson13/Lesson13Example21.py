#use + operator
varCarList1=["Dodge", "Ford", "Toyota"]
varCarList2=["Honda","BMW"]
varCarList3=["Alfa Romeo", "Chevrolet"]
varCarList4 = varCarList1+varCarList2
print(varCarList4)
#use extend method
varCarList1.extend(varCarList3)
print(varCarList1)
#use for cycle to append items
for car in varCarList3:
    varCarList2.append(car)
    
print(varCarList2)
