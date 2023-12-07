varNum1 = 5 #101
varNum2 = 2 #010
varNum3 = 3 #011
result1 = varNum1&varNum2 #000
print(result1) #0
result2 = varNum1|varNum2 #111 - 7
print(result2) #7
result3 = varNum1^varNum2 #111 - 7
print(result3)
result4 = ~varNum2 #101 -3
print(result4) #-3
result5 = varNum1<<varNum2 #10100 - 20
print(result5) #20
result6 = result5>>2 #101 - 5
print(result6)
#101&
#011
#001
result7 = varNum1&varNum3 #101&011 = 001
print(result7) #1
#101 |
#011
#111
result8 = varNum1|varNum2 #111
print(result8) #7

