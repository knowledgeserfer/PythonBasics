#The __str__() function controls what should be returned 
#when the class object is represented as a string.
#If the __str__() function is not set, the string representation 
#of the object is returned.
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        
person1 = Person("John", "Smith", 35)
print(person1)
print(person1.name, person1.surname, person1.age)
person2 = Person("Jenny", "Jackson", 30)
print(person2)
print(person2.name, person2.surname, person2.age)

