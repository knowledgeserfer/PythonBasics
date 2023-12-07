#To understand the meaning of classes we have to understand 
#the built-in __init__() function.
#All classes have a function called __init__(), which is always 
#executed when the class is being initiated.
#The __init__() function is called automatically every time 
#the class is being used to create a new object.
class MyFavouriteNumber:
    def __init__(self, favouriteNumber):
        self.favouriteNumber=favouriteNumber
        
favNum1 = MyFavouriteNumber(7)

print(favNum1.favouriteNumber)

favNum2 = MyFavouriteNumber(8)

print(favNum2.favouriteNumber)





