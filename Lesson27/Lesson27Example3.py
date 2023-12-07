#To prevent the iteration from going on forever, we can use 
#the StopIteration statement.
class IncreaseByOne:
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        if self.num<=10:
            nextnum = self.num
            self.num += 1
            return nextnum
        else:
            raise StopIteration
    
instance1 = IncreaseByOne()
iterator1 = iter(instance1)
for i in iterator1:
    print(i)