#If we call the function without argument, 
#it uses the default value
def greeting_function(name="James"):
    print("Hello {}!".format(name))
    
greeting_function("Walter")
greeting_function()

