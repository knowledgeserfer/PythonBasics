import re
str1 = "25th December. It was raining outside."
print("Return a match at every no-digit character")
searchResult = re.findall("\D", str1)
print(searchResult)
print("Return a match at every white-space character")
searchResult2 = re.findall("\s", str1)
print(searchResult2)
print("Return a match at every NON white-space character")
searchResult3 = re.findall("\S", str1)
print(searchResult3)
print("Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character)")
searchResult4 = re.findall("\w", str1)
print(searchResult4)
print("Return a match at every NON word character (characters NOT between a and Z. Like \"!\", \"?\" white-space etc.)")
searchResult5 = re.findall("\W", str1)
print(searchResult5)
print("Check if the string ends with \"outside.\"")
searchResult6 = re.findall("outside.\Z", str1)
print(searchResult6)