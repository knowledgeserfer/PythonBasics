#Why do we need inheritance
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
person1 = Person("John", "Smith")
student1 = Student("Jenny", "Jackson")
print(person1.name, person1.surname)
print(student1.name,student1.surname)


