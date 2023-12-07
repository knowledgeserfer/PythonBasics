#A RegEx, or Regular Expression, is a sequence of characters that forms 
#a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.
#Python has a built-in package called re, which can be used to work with 
#Regular Expressions.
#Import the re module.
#findall() function returns a list containing all matches.
import re

str1 = "It was raining outside."
mathcList = re.findall("rain", str1)
print(str1)
print(mathcList)





