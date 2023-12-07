import re

str1 = "15th December. It was raining outside."
#Find all lower case characters alphabetically between "a" and "y":
searchResult = re.findall("[a-y]", str1)
print("All lower case characters")
print(searchResult)
#Find all digit characters:
searchResult2 = re.findall("\d", str1)
print(searchResult2)
#Search for a sequence that starts with "ra", followed by four (any) 
#characters, and an "g":
searchResult3 = re.findall("ra....g", str1)
print(searchResult3)

