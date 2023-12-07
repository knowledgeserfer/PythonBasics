#In Python, a generator is a function that returns an iterator
#We can define a generator function using the def keyword, 
#but instead of the return statement we use the yield statement.
#The yield keyword is used to produce a value from the generator.
#When the generator function is called, it does not execute the 
#function body immediately. Instead, it returns a generator object 
#that can be iterated over to produce the values.
def increaseByOneGenerator(n):
    num = 0
    while num<n:
        yield num
        num+=1
        
for i in increaseByOneGenerator(10):
    print(i)
print("---------------")
generator1 = increaseByOneGenerator(25)
print(next(generator1))
print(next(generator1))
print(next(generator1))
for i in generator1:
    print(i)