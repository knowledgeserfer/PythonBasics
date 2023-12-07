class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age
        
    def displayFunc(self):
        print(f"Name:{self.__name} Surname:{self.__surname} Age:{self.__age}")
        
person1 = Person("John", "Smith", 35)
person1.displayFunc()
person1.__name = "James"
person1.__surname = "Johns"
person1.__age = 25
print("--------------")
person1.displayFunc()
print(person1.__age)
print(person1.__surname)
print(person1.__name)
person2 = Person("Jenny", "Jackson", 30)
person2.displayFunc()
print(person2.__age)