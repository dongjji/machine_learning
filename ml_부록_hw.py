#1
import numpy as np
arr = np.array([[4, 2, 0], [2, 4, 4,], [0, 4, 8]])
arr_inv = np.linalg.inv(arr)
argmin_J = np.linalg.inv(arr)@np.array([[1], [1], [1]])
print(arr_inv)
print(argmin_J)

#1-1
arr2 = np.array([[8, 4, 0], [4, 8, 8], [0, 8, 16]])
arr2_inv = np.linalg.inv(arr2)
argmin_J2 = np.linalg.inv(arr2)@np.array([[-2], [-2], [-2]])
print(arr2_inv)
print(argmin_J2)