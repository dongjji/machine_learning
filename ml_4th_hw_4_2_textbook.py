import numpy as np

EN = [77, 81, 74, 89, 78, 77, 75, 84, 79, 82, 69, 76, 74, 67, 74, 71, 67, 67, 70, 69]
MATH = [72, 67, 74, 64, 71, 67, 72, 68, 75, 70, 83, 78, 76, 82, 80, 77, 83, 84, 80, 80]
SCIENCE = [75, 68, 72, 68, 74, 68, 75, 73, 79, 72, 78, 75, 72, 74, 77, 70, 75, 79, 77, 76]

y = np.array(EN)
x = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], MATH, SCIENCE])

Rxx = x@x.T/20
rxy = x@(y.T)/20
INV_Rxx = np.linalg.inv(Rxx)
opt_param = INV_Rxx@rxy

print("상관 행렬:\n", Rxx)
print("상호 상관 행렬:\n",rxy)

print("상관 행렬의 역행렬:\n",INV_Rxx)
print("최적 파라미터 세타:\n", opt_param)