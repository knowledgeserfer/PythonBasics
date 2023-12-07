#Class attributes are accessible by defalt, which means you can change them.
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        
    def displayFunc(self):
        print(f"Name: {self.name} Surname:{self.surname} Age:{self.age}")
        
person1 = Person("John", "Smith", 35)
person1.displayFunc()
person1.age = -200
person1.surname = "InvalidSurname"
person1.name = "InvalidName"
person1.displayFunc()
print(person1.surname)

