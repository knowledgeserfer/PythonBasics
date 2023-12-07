#The self parameter is a reference to the current instance of the class, 
#and is used to access variables that belongs to the class.
#It does not have to be named self , you can call it whatever you like, 
#but it has to be the first parameter of any function in the class.
class Person:
    def __init__(refToCurrentInstance, name, surname):
        refToCurrentInstance.name = name
        refToCurrentInstance.surname = surname
        
    def introduceFunc(refToCurrentInstance):
        print("Hello my name is {} {}".format(refToCurrentInstance.name,
                                              refToCurrentInstance.surname))
        
person1  = Person("John", "Smith")
person1.introduceFunc()
person2 = Person("Jenny", "Jackson")
person2.introduceFunc()



