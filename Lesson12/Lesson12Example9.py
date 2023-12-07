#To let a function return a value, use the return statement
def multiply_by_itself(num1):
    return num1*num1

result1 = multiply_by_itself(3)
print(result1)
result2 = multiply_by_itself(5)
print(result2)
result3 = multiply_by_itself(7)
print(result3)

#function definitions cannot be empty, but if you 
#for some reason have a function definition with no content, 
#put in the pass statement to avoid getting an error.
def greeting_function():
    pass