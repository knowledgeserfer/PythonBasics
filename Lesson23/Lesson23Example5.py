#Objects can also contain methods. Methods in objects are functions 
#that belong to the object.
#The self parameter is a reference to the current instance of the class, 
#and is used to access variables that belong to the class.
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def introduceFunc(self):
        print("Hello my name is {} {}".format(self.name, self.surname))
        
person1 = Person("John", "Smith")
person1.introduceFunc()
person2 = Person("Jenny", "Jackson")
person2.introduceFunc()


