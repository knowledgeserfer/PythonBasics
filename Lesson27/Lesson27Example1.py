#An iterator is an object that contains a countable number of values.
#An iterator is an object that can be iterated upon, meaning 
#that you can traverse through all the values.
#In Python, an iterator is an object which implements the iterator protocol, 
#which consist of the methods __iter__() and __next__().
#Lists, tuples, dictionaries, and sets are all iterable objects.
str1 = "Text"
str1Iterator = iter(str1)
print(str1Iterator)
print(next(str1Iterator))
print(next(str1Iterator))
print(next(str1Iterator))
print(next(str1Iterator))
#print(next(str1Iterator))
list1 = ["Dodge", "Ford", "Toyota"]
list1Iterator = iter(list1)
print(list1Iterator)
print(next(list1Iterator))
print(next(list1Iterator))
print(next(list1Iterator))
for i in list1:
    print(i)