#To create an object/class as an iterator you have to implement 
#the methods __iter__() and __next__() to your object.
#The __iter__() method must always return the iterator object itself.
#The __next__() method also allows you to do operations, 
#and must return the next item in the sequence.
class IncreaseByOne:
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        nextnum = self.num
        self.num += 1
        return nextnum
    
instance1 = IncreaseByOne()
iterator1 = iter(instance1)
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
