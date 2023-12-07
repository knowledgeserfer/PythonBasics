#.span() returns a tuple containing the start-, and end positions 
#of the match.
#The regular expression looks for any words that starts with an lower case "r"
import re

str1 = "It was raining outside."
searchResult = re.search(r"\br\w+", str1)
print(searchResult)
print(searchResult.span())



