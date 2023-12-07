#If you do not know how many keyword arguments that 
#will be passed into your function, add 
#two asterisk: ** before the parameter name in the function 
#definition.
#This way the function will receive a dictionary of arguments, 
#and can access the items accordingly
def greeting_function(**names):
    print("Hello {}, {}!".format(names["name1"], names["name2"]))
    
greeting_function(name1 = "Skyler", name2 = "Walter")

