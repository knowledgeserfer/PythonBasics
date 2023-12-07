#The search() function searches the string for a match, and returns a 
#Match object if there is a match.
#If there is more than one match, only the first occurrence of the match 
#will be returned.
import re

str1 = "It was raining outside."
match1 = re.search("\s", str1)
print(match1)
print("Position of space: ", match1.start())




