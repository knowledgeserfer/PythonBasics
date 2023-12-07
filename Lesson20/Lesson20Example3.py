#The datetime object has a method for formatting date objects 
#into readable strings.
#The method is called strftime(), and takes one parameter, format, 
#to specify the format of the returned string
import datetime

date1 = datetime.datetime(2020,12,25,9,50,55,10)

print(date1.year)
print(date1.month)
print(date1.strftime("%A"))#prints full version of weekday
print(date1.strftime("%w"))#prints weekday as number 0-6, 0 - Sunday
print(date1.strftime("%B"))#prints months name, e.g. December
print(date1.strftime("%I"))#prints hours 00-12
print(date1.strftime("%u"))#ISO 8601 weekday
