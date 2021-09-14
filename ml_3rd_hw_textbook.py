import numpy as np
from sklearn.decomposition import PCA

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
       
PCC_EN_MATH = np.corrcoef(EN, MATH)
PCC_EN_SC = np.corrcoef(EN, SCIENCE)
PCC_MATH_SC = np.corrcoef(MATH, SCIENCE)

print(PCC_EN_MATH)
print(PCC_EN_SC)
print(PCC_MATH_SC)


# 3.4
pca = PCA(whiten=True)
whitened = pca.fit_transform([[2, 2], [2, 4]])
print(whitened)