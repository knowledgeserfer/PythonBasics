import numpy as np

numArray = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(numArray)
print("Dimensions number equals {}".format(numArray.ndim))
print("Size of array is {}".format(numArray.size))

print("Element from array {}".format(numArray[0][1][0]))
print("Element from array {}".format(numArray[0][1][1]))
print("Element from array {}".format(numArray[1][0][0]))
print("Element from array {}".format(numArray[1][1][0]))

for i in numArray:
    for j in i:
        for k in j:
            print(k)
            



