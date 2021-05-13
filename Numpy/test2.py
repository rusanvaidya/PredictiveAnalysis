import numpy as np

# arr = np.array([
#     [1, 2, 2],
#     [9, 1, 5],
#     [4, 8, 3]
# ])
# print(arr, "\n")
#
# # For one-dimensional array
# print("Slicing the array : ")
# print(arr[2:3], "\n")
#
# # For 2 dimensional
# print("For 2-D : ")
# print(arr[1:3, 1:2])
#
# print("\n Change value : ")
# arr1 = arr[2:3]
# print(arr1)
# arr1[:] = 7
#
# print("\n Original : ")
# print(arr)

# print("\n Copying : ")
# print("\n Change value : ")
# arr1 = arr[2:3].copy()
# print(arr1)
# arr1[:] = 7

# print("\n Original : ")
# print(arr)
# print(np.exp(arr))
# print("\n")
# print(np.square(arr))

# arr3 = np.array([
#     [1, 2, 3]
# ])
#
# arr4 = np.array([
#     [1],
#     [2],
#     [3]
# ])
# print(arr3 + arr4)
# print(np.add(arr3, arr4))
# print(np.subtract(arr3, arr4))
# print(np.sqrt(arr3))
# print(np.cbrt(arr3))

# print(np.where(arr3>arr4,arr3,arr4))

# arr5 = np.random.rand(7)
# print(arr5)
# print("MEAN : ", np.mean(arr5))
# print("VARIANCE : ", np.var(arr5))
# print("STANDARD : ", np.std(arr5))
# print("SUM : ", np.sum(arr5))

# print(np.unique(arr5))
# print(np.any(arr5))
# np.save("arr5.npy",arr5)

# arr0 = np.load("arr5.npy")
# print(arr0)
#
# def getMinMax(arr):
#     res = []
#     for i in range(arr.shape[0]):
#         res.append(arr[i].min())
#         res.append(arr[i].max())
#     return res
#
# arr6 = np.arange(9)
# arr7 = getMinMax(arr6)
# print(arr7)

import numpy as np
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr[1:3,1:3])



