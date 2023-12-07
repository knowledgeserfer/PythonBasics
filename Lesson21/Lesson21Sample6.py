import re
str1 = "25th December. It was raining outside."
#Check if the string has any j, i, or w characters
searchResult = re.findall("[jiw]", str1)
print(searchResult)
#Check if the string has any characters between j and w
searchResult2 = re.findall("[j-w]", str1)
print(searchResult2)
#Check if the string has other characters than j, i, or w
searchResult3 = re.findall("[^jiw]", str1)
print(searchResult3)
#Check if the string has any 1, 2, 3, 4 or 5 digits
searchResult4 = re.findall("[12345]", str1)
print(searchResult4)
