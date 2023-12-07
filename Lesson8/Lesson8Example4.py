varCondition1 = 5>2 #True
varCondition2 = 3==0 #False
varCondition3 = 3!=0 #True
complexConditionRes1 = varCondition1 and varCondition2 #False
print(complexConditionRes1)
complexConditionRes2 = varCondition1 and varCondition3 #True
print(complexConditionRes2)
complexConditionRes3 = varCondition1 or varCondition2 #True
print(complexConditionRes3)
complexConditionRes4 = varCondition2 or 3>5 #False
print(complexConditionRes4)
conditionRes1 = not(varCondition2)#True
print(conditionRes1)
