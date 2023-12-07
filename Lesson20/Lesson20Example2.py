#To create a date, we can use the datetime() class (constructor) 
#of the datetime module.
#The datetime() class requires three parameters to create a date: 
#year, month, day.
#The datetime() class also takes parameters for time and timezone 
#(hour, minute, second, microsecond, tzone), but they are optional, 
#and has a default value of 0, (None for timezone).
import datetime

date1 = datetime.datetime(2020, 12, 25, 9, 45, 50, 10)

print(date1)

