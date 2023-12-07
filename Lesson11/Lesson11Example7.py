#A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration 
#of the "outer loop"
carList1 = ["Dodge","Ford","Toyota"]
carList2 = ["Charger", "Focus", "Camry"]
for car1 in carList1:
    for car2 in carList2:
        print(car1, car2)

