#The frozenset() function returns an unchangeable frozenset object
varCarSet = {"Dodge", "Ford", "Toyota"}
print(varCarSet)
varCarSet.add("Lincoln")
print(varCarSet)

frozenVarCarSet = frozenset(varCarSet)
print(frozenVarCarSet)
#frozenVarCarSet.pop("Ford")
#frozenVarCarSet.add("Chrysler")

