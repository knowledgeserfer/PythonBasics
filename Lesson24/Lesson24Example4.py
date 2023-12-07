class Person:
    def __init__(self, surname, age):
        self.__surname = surname
        self.__age = age
        
    #setter method
    def setAge(self, age):
        if 1<age<120:
            self.__age=age
            
        else:
            print("Invalid age input.")
    #getter method            
    def getAge(self):
        return self.__age

person1 = Person("Smith", 35)
print(person1.getAge())
person1.setAge(33)
print(person1.getAge())
person1.setAge(0)
print(person1.getAge())
print(person1.__surname)