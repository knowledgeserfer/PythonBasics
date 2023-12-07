#The string representation of an object WITH the __str__() function
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        
    def __str__(self):
        return f"Name: {self.name} Surname: {self.surname} Age: {self.age}"

        
person1 = Person("John", "Smith", 35)
print(person1)
person2 = Person("Jenny", "Jackson", 30)
print(person2)

