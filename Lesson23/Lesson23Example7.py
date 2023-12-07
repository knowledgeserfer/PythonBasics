#You can modify properties on objects using dot syntax for access
class Person:
    def __init__(self, name, surname, age):
        self.name =  name
        self.surname =  surname
        self.age = age
        
    def introduceFunc(self):
        print("Hello my name is {} {}".format(self.name, self.surname))
        print("I'm {} old".format(self.age))
        

person1 = Person("John", "Smith", 35)
person1.introduceFunc()
person1.name = "James"
person1.age = 33
person1.introduceFunc()
del person1.age
#person1.introduceFunc()
del person1
#print(person1)
