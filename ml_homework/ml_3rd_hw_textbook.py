import numpy as np

CXX_EN_MATH = [
  [35.2, -31.95],
  [-31.95, 35.2275]
]

CXX_EN_SC = [
  [35.2, -10.7],
  [-10.7, 11.4275]
]

CXX_MATH_SC = [
  [35.2275, 14.6725],
  [14.6725, 11.4275]
]

EN = [77, 81, 74, 89, 78, 77, 75, 84, 79, 82, 69, 76, 74, 67, 74, 71, 67, 67, 70, 69]
MATH = [72, 67, 74, 64, 71, 67, 72, 68, 75, 70, 83, 78, 76, 82, 80, 77, 83, 84, 80, 80]
SCIENCE = [75, 68, 72, 68, 74, 68, 75, 73, 79, 72, 78, 75, 72, 74, 77, 70, 75, 79, 77, 76]

EN_A = np.array([77, 81, 74, 89, 78, 77, 75, 84, 79, 82])
MATH_A = np.array([72, 67, 74, 64, 71, 67, 72, 68, 75, 70])
SC_A = np.array([75, 68, 72, 68, 74, 68, 75, 73, 79, 72])

EN_B = np.array([69, 76, 74, 67, 74, 71, 67, 67, 70, 69])  
MATH_B = np.array([83, 78, 76, 82, 80, 77, 83, 84, 80, 80])
SC_B = np.array([78, 75, 72, 74, 77, 70, 75, 79, 77, 76])

MEAN_A_EN_MATH = np.mean([EN_A, MATH_A], axis=1).reshape(2,1)
MEAN_A_EN_SC = np.mean([EN_A, SC_A], axis=1).reshape(2,1)
MEAN_A_MATH_SC = np.mean([MATH_A, SC_A], axis=1).reshape(2,1)

MEAN_B_EN_MATH = np.mean([EN_B, MATH_B], axis=1).reshape(2,1)
MEAN_B_EN_SC = np.mean([EN_B, SC_B], axis=1).reshape(2,1)
MEAN_B_MATH_SC = np.mean([MATH_B, SC_B], axis=1).reshape(2,1)

def COR(X, XT, N):
    return X@XT/N
  
def COV(COR, MMT):
  return COR - MMT

def MMT(MEAN):
  return MEAN@MEAN.T

A_EN_MATH = np.array([EN_A, MATH_A])
A_EN_SC = np.array([EN_A, SC_A])
A_MATH_SC = np.array([MATH_A, SC_A])
B_EN_MATH = np.array([EN_B, MATH_B])
B_EN_SC = np.array([EN_B, SC_B])
B_MATH_SC = np.array([MATH_B, SC_B])

COR_A_EN_MATH = COR(A_EN_MATH, A_EN_MATH.T, len(A_EN_MATH[0]))
COR_A_EN_SC = COR(A_EN_SC, A_EN_SC.T, len(A_EN_SC[0]))
COR_A_MATH_SC = COR(A_MATH_SC, A_MATH_SC.T, len(A_MATH_SC[0]))

COR_B_EN_MATH = COR(B_EN_MATH, B_EN_MATH.T, len(B_EN_MATH[0]))
COR_B_EN_SC = COR(B_EN_SC, B_EN_SC.T, len(B_EN_SC[0]))
COR_B_MATH_SC = COR(B_MATH_SC, B_MATH_SC.T, len(B_MATH_SC[0]))

COV_A_EN_MATH = COV(COR_A_EN_MATH, MMT(MEAN_A_EN_MATH))
COV_A_EN_SC = COV(COR_A_EN_SC, MMT(MEAN_A_EN_SC))
COV_A_MATH_SC = COV(COR_A_MATH_SC, MMT(MEAN_A_MATH_SC)) 

COV_B_EN_MATH = COV(COR_B_EN_MATH, MMT(MEAN_B_EN_MATH))
COV_B_EN_SC = COV(COR_B_EN_SC, MMT(MEAN_B_EN_SC))
COV_B_MATH_SC = COV(COR_B_MATH_SC, MMT(MEAN_B_MATH_SC)) 

PCC_A_EN_MATH = np.corrcoef(EN_A, MATH_A)
PCC_A_EN_SC = np.corrcoef(EN_A, SC_A)
PCC_A_MATH_SC = np.corrcoef(MATH_A, SC_A)

PCC_B_EN_MATH = np.corrcoef(EN_B, MATH_B)
PCC_B_EN_SC = np.corrcoef(EN_B, SC_B)
PCC_B_MATH_SC = np.corrcoef(MATH_B, SC_B)

print("Covariance of groupA with English and Math: \n{}\n".format(COV_A_EN_MATH))
print("Covariance of groupA with English and Science: \n{}\n".format(COV_A_EN_SC))
print("Covariance of groupA with Math and Science: \n{}\n".format(COV_A_MATH_SC))

print("Covariance of groupB with English and Math: \n{}\n".format(COV_B_EN_MATH))
print("Covariance of groupB with English and Science: \n{}\n".format(COV_B_EN_SC))
print("Covariance of groupB with Math and Science: \n{}\n".format(COV_B_MATH_SC))

PCC_EN_MATH = np.corrcoef(EN, MATH)
PCC_EN_SC = np.corrcoef(EN, SCIENCE)
PCC_MATH_SC = np.corrcoef(MATH, SCIENCE)

print("Pearson's correlation coefficient of All with English and Math: \n{}\n".format(PCC_EN_MATH))
print("Pearson's correlation coefficient of All with English and Science: \n{}\n".format(PCC_EN_SC))
print("Pearson's correlation coefficient of All with Math and Science: \n{}\n".format(PCC_MATH_SC))

print("Pearson's correlation coefficient of groupA with English and Math: \n{}\n".format(PCC_A_EN_MATH))
print("Pearson's correlation coefficient of groupA with English and Science: \n{}\n".format(PCC_A_EN_SC))
print("Pearson's correlation coefficient of groupA with Math and Science: \n{}\n".format(PCC_A_MATH_SC))

print("Pearson's correlation coefficient of groupB 1with English and Math: \n{}\n".format(PCC_B_EN_MATH))
print("Pearson's correlation coefficient of groupB with English and Science: \n{}\n".format(PCC_B_EN_SC))
print("Pearson's correlation coefficient of groupB with Math and Science: \n{}\n".format(PCC_B_MATH_SC))


# 3.4
cov = np.array([[2, 2], [2, 4]])
def whiten(X):
  U, S, U_T= np.linalg.svd(X)
  UNIT_MATRIX = np.dot(U, U.T) # I
  print("EigenVector of Covariance: \n{}\n".format(U)) # EigenVectors
  print("EigenValues of Covariance1: \n{}\n".format(S)) # EigenValues
  print("EigenValues of Covariance2: \n{}\n".format(np.dot(np.dot(U.T, X), U))) # EigenValues
  
  V = np.dot(1/np.sqrt(S), U.T)
  
  return V
  
print("V for whitening z vector: \n{}\n".format(whiten(cov)))