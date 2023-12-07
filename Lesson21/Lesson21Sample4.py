import re
str1 = "25th December. It was raining outside."
#Check if the string starts with "It"
searchResult = re.findall("\AIt", str1)
print(searchResult)
#Check if "rain" is present at the beginning of a word
searchResult2 = re.findall(r"\brain", str1)
print(searchResult2)
#Check if "ing" is present at the end of a word
searchResult3 = re.findall(r"ing\b", str1)
print(searchResult3)
#Check if "ini" is present, but NOT at the beginning of a word
searchResult4 = re.findall(r"\Bini", str1)
print(searchResult4)
#Check if the string contains any digits (numbers from 0-9)
searchResult5 = re.findall("\d", str1)
print(searchResult5)

