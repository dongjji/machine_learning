import numpy as np
x3 = [
      [77, 81, 74, 89, 78, 77, 75, 84, 79, 82, 69, 76, 74, 67, 74, 71, 67, 67, 70, 69],
      [72, 67, 74, 64, 71, 67, 72, 68, 75, 70, 83, 78, 76, 82, 80, 77, 83, 84, 80, 80],
      [75, 68, 72, 68, 74, 68, 75, 73, 79, 72, 78, 75, 72, 74, 77, 70, 75, 79, 77, 76] 
    ]

X = np.array(x3)
# Mean
MEAN_X = np.mean(X, axis=1).reshape(3, 1)
print("Mean: \n{}\n".format(MEAN_X))
# Mean^T
MEAN_XT = MEAN_X.T
print("MeanT: \n{}\n".format(MEAN_X.T))
# Mean dot Mean^T
MMT = MEAN_X@MEAN_X.T
print("Mean@Mean^T: \n{}\n".format(MMT))


# # Covariance
# cov_x3 = np.cov(X)
# print("Covariance: \n{}\n".format(cov_x3))

# Correlation
XXT = X@X.T
def COR(X, XT, N):
    return X@XT/N

COR_X = COR(X, X.T, len(X[0]))
print("Correlation: \n {}\n".format(COR_X))

# Covarriance
def COV(COR, MMT):
    return COR - MMT

COV_X = COV(COR_X, MMT)
print("Covariance: \n{}\n".format(COV_X))

print("RXX^-1: \n{}".format(np.linalg.inv(COR_X)))
print("CXX^-1: \n{}".format(np.linalg.inv(COV_X)))

# print("RXX^-1: \n{}".format(np.linalg.inv([[2/3, 1/3], [1/3, 2/3]])))
# print("CXX^-1: \n{}".format(np.linalg.inv([[2/9, -1/9], [-1/9, 2/9]])))


