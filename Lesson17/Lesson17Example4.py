import numpy as np

numArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(numArray)
print("Dimensions number equals {}".format(numArray.ndim))
print("Size of array is {}".format(numArray.size))

for i in numArray:
    for j in i:
        print(j)
        
