#Generator comprehension
#expression for item in iterable
#The generator expression creates a generator object that produces 
#the values of expression for each item in the iterable object, 
#one at a time during each iteration.
squareGenerator = (num*num for num in range(10))
for i in squareGenerator:
    print(i)
    

