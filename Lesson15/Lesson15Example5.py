#You cannot access items in a set by referring 
#to an index or a key.
#But you can loop through the set items using a for loop.
varCarSet = {"Dodge", "Ford", "Toyota", "BMW", "Lincoln"}
for car in varCarSet:
    print(car)
    
if "Lincoln" in varCarSet:
    print("Lincoln is in varCarSet")
    
else:
    print("Lincoln is not in varCarSet")
