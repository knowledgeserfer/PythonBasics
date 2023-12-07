import re
str1 = "25th December. It was raining outside.+"
#Check if the string has any digits between 0 and 9
searchResult = re.findall("[0-9]", str1)
print(searchResult)
#Check if the string has any two-digit numbers, from 00 to 99
searchResult2 = re.findall("[0-9][0-9]", str1)
print(searchResult2)
#Check if the string has any characters from a to w lower case, 
#and A to Y upper case
searchResult3 = re.findall("[a-wA-Y]", str1)
print(searchResult3)
#Check if the string has any + characters
searchResult4 = re.findall("[+]", str1)
print(searchResult4)
