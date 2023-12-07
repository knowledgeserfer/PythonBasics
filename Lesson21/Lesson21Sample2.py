import re

str1 = "It was raining outside."
#Check if the string starts with 'It':
searchResult = re.findall("^It", str1)
print(searchResult)
#Check if the string ends with 'side.':
searchResult2 = re.findall("side.$", str1)
print(searchResult2)
#Search for a sequence that starts with "ra", followed by 0 
#or more characters, and an "g":
searchResult3 = re.findall("ra.*g", str1)
print(searchResult3)