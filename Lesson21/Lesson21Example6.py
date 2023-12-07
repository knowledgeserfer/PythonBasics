#You can control the number of occurrences by specifying 
#the maxsplit parameter
import re

str1 = "It was raining outside."
splitedList = re.split("\s", str1, 1)
print(str1)
print(splitedList)

