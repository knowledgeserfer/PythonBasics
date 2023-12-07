#The word "polymorphism" means "many forms", and in programming it 
#refers to methods/functions/operators with the same name that 
#can be executed on many objects or classes.
class Cat:
    def sound(self):
        print("Meow, meow, meow")
        
class Dog:
    def sound(self):
        print("Woof, woof, woof")
        
cat1 = Cat()
dog1 = Dog()
cat1.sound()
dog1.sound()
