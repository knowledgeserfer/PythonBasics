#Global keyword
def greetingFunction():
    global name
    name = "James"
    print("Hello, my name is ", name)
    
greetingFunction()
print("My name is ", name)
