#If you do not know how many arguments that will be passed 
#into your function, add a * before the parameter name 
#in the function definition
#This way the function will receive a tuple of arguments, 
#and can access the items accordingly
def greeting_function(*namesVar):
    print("Hello {}, {}".format(namesVar[0], namesVar[1]))
    
greeting_function("Walter", "Skyler")

