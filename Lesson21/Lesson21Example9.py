#A Match Object is an object containing information about the search 
#and the result.
#If there is no match, the value None will be returned, instead of 
#the Match Object.
import re

str1 = "It was raining outside."
searchResult = re.search("rain", str1)
print(searchResult)


