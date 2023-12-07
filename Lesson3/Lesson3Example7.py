#Global variables: variable with same name inside function
name = "James"
def greetingFunction():
    name = "Jenny"
    print("Hello, my name is ", name)
    
greetingFunction()

print("My name is ", name)


