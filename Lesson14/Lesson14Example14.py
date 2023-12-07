#If the number of variables is less than the number of values, 
#you can add an * to the variable name and the values 
#will be assigned to the variable as a list
varCarTuple1 = ("Dodge", "Ford", "Toyota", "Lincoln", "BMW")
print(varCarTuple1)
(car1, car2, *car3) = varCarTuple1
print(car1)
print(car2)
print(car3)


