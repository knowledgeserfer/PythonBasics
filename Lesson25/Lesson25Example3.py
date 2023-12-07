#Python also has a super() function that will make the child class 
#inherit all the methods and properties from its parent.
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
class Student(Person):
    def __init__(self, name, surname, averageMark):
        super().__init__(name, surname)
        self.averageMark = averageMark
        
person1 = Person("John", "Smith")
student1 = Student("Jenny", "Jackson", 3.5)
print(person1.name, person1.surname)
print(student1.name,student1.surname, student1.averageMark)
