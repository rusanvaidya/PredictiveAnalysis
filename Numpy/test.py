import numpy as np

# arr = np.arange(0,10,1) # Generate array with numbers from 0 to 9
# print("The Array")
# print(arr)
#
# print("\nElement at index 5")
# print(arr[5]) # Fetch element at index 5
#
# print("\nElements in a range of 0 to 6")
# print(arr[0:6]) # Fetch elements in a range
#
# arr[0:6] = 20 # Assign a value to a range of elements
# print("\nNew array after changing elements in a range of 0 to 6")
# print(arr.shape())

x = np.linspace(0, 10, 100)
y = np.array(x).reshape(1, 100)
print(y.shape)
