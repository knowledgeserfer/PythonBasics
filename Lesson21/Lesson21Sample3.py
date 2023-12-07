import re
str1 = "It was raining outside."
#Search for a sequence that starts with "ra", followed by 1 or more  
#(any) characters, and an "g"
searchResult = re.findall("ra.+g", str1)
print(searchResult)
#Search for a sequence that starts with "ra", followed by 0 or 1 
#character, and an "o":
searchResult2 = re.findall("ra.?g", str1)
print(searchResult2)
#Search for a sequence that starts with "ra", followed excactly 
#4 characters, and an "g"
searchResult3 = re.findall("ra.{4}g",str1)
print(searchResult3)
#Check if the string contains either "raining" or "snowing"
searchResult4 = re.findall("raining|snowing",str1)
print(searchResult4)


