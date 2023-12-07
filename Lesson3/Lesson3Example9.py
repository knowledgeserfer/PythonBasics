
#Global keyword
name = "James"
def greetingFunction():
    global name
    name = "Jenny"
    print("Hello, my name is ", name)
    
greetingFunction()
print("My name is ", name)
