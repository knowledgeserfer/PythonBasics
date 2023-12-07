#To create a getter property use @property annotation.
#To create a setter property use @name.setter annotation.
class Person:
    def __init__(self, surname, age):
        self.__surname = surname
        self.__age = age
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if 1<age<120:
            self.__age=age    
        else:
            print("Invalid age input.")
            
person1 = Person("Smith", 35)
print(person1.age)
person1.age = 33
print(person1.age)
person1.age = 150
print(person1.age)

