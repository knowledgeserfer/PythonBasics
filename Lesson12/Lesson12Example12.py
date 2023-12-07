#The power of lambda is better shown when you use them as 
#an anonymous function inside another function.
def my_function(num1):
    return lambda unknownNum : unknownNum * num1

doubleNum = my_function(2)
print("Doubled results")
print(doubleNum(1))
print(doubleNum(5))
print(doubleNum(10))

numByFive = my_function(5)
print("Multiplied by five results")
print(numByFive(5))
print(numByFive(10))


