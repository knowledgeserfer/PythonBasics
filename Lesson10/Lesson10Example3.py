#With the continue statement we can stop the current iteration, 
#and continue with the next
iterationVar = 1
while iterationVar <= 5:
    if iterationVar == 3:
        iterationVar+=1
        continue
    print("iterationVar equals ", iterationVar)
    iterationVar+=1
    


