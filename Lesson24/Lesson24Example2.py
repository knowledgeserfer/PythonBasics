#We can protect variables in the class by marking them private. 
#To define a private variable add two underscores as a prefix 
#at the start of a variable name.
#self.__age
class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age
        
    def displayFunc(self):
        print(f"Name:{self.__name} Surname:{self.__surname} Age:{self.__age}")
        
person1 = Person("John", "Smith", 35)
person1.displayFunc()
#print(person1.__age)
#print(person1.__surname)
#print(person1.__name)