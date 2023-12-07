#You can control the number of replacements by specifying the count parameter
import re

str1 = "It was raining outside."
substitutedStr1 = re.sub("\s", "-", str1, 1)

print(str1)
print(substitutedStr1)



