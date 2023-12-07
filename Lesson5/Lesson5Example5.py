#complex numbres can not be converted to another
#number type
intVariable1 = 8
floatVariable1 = 9.5
complexVariable1 = 7j

intVariable2 = int(floatVariable1)
floatVariable2 = float(intVariable1)
complexVariable2 = complex(floatVariable1)
#intVariable3 = int(complexVariable1)
print(intVariable2, type(intVariable2))
print(floatVariable2, type(floatVariable2))
print(complexVariable2, type(complexVariable2))
