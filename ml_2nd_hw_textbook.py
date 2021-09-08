import numpy as np

groupA = np.array([
    [77, 81, 74, 89, 78, 77, 75, 84, 79, 82],
    [72, 67, 74, 64, 71, 67, 72, 68, 75, 70],
    [75, 68, 72, 68, 74, 68, 75, 73, 79, 72]
])

groupB = np.array([
    [69, 76, 74, 67, 74, 71, 67, 67, 70, 69],
    [83, 78, 76, 82, 80, 77, 83, 84, 80, 80],
    [78, 75, 72, 74, 77, 70, 75, 79, 77, 76]
])

MEAN_A = np.mean(groupA, axis=1).reshape(3, 1)
MEAN_B = np.mean(groupB, axis=1).reshape(3, 1)
MMT_A = MEAN_A@MEAN_A.T
MMT_B = MEAN_B@MEAN_B.T

# Correlation
def COR(X, XT, N):
    return X@XT/N
# Covarriance
def COV(COR, MMT):
    return COR - MMT

COR_A = COR(groupA, groupA.T, len(groupA[0]))
COR_B = COR(groupB, groupB.T, len(groupB[0]))
COV_A = COV(COR_A, MMT_A)
COV_B = COV(COR_B, MMT_B)

print("MEAN_A: \n{}\n".format(MEAN_A))
print("MEAN_A.T: \n{}\n".format(MEAN_A.T))
print("MMT_A: \n{}\n".format(MMT_A))
print("Correlation RXX_A: \n {}\n".format(COR_A))
print("Covariance CXX_A: \n{}\n".format(COV_A))
print("INV_RXX_A: \n{}\n".format(np.linalg.inv(COR_A)))
print("INV_CXX_A: \n{}\n".format(np.linalg.inv(COV_A)))

print("MEAN_B: \n{}\n".format(MEAN_B))
print("MEAN_B.T: \n{}\n".format(MEAN_B.T))
print("MMT_B: \n{}\n".format(MMT_B))
print("Correlation RXX_B: \n {}\n".format(COR_B))
print("Covariance CXX_B: \n{}\n".format(COV_B))
print("INV_RXX_A: \n{}\n".format(np.linalg.inv(COR_B)))
print("INV_CXX_A: \n{}\n".format(np.linalg.inv(COV_B)))