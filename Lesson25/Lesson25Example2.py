#Inheritance allows us to define a class that inherits all the methods 
#and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, 
#also called derived class.
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
class Student(Person):
    pass
        
person1 = Person("John", "Smith")
student1 = Student("Jenny", "Jackson")
print(person1.name, person1.surname)
print(student1.name,student1.surname)
