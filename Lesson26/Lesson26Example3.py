#We can use Polymorphism with inheritance classes
class Animal:
    def sound(self):
        print("Animal sound")
    
class Cat(Animal):
    def sound(self):
        print("Meow")
        
class Dog(Animal):
    def sound(self):
        print("Woof")
        
cat1 = Cat()
dog1 = Dog()
cat1.sound()
dog1.sound()
