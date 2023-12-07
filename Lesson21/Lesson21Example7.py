#The sub() function replaces the matches with the text of your choice
import re

str1 = "It was raining outside."
substitutedStr1 = re.sub("\s", "-", str1)

print(str1)
print(substitutedStr1)

