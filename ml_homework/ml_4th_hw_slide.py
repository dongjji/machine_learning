import pandas as pd
import numpy as np
# from sklearn.linear_model import LinearRegression

EN = [77, 81, 74, 89, 78, 77, 75, 84, 79, 82, 69, 76, 74, 67, 74, 71, 67, 67, 70, 69]
MATH = [72, 67, 74, 64, 71, 67, 72, 68, 75, 70, 83, 78, 76, 82, 80, 77, 83, 84, 80, 80]
SCIENCE = [75, 68, 72, 68, 74, 68, 75, 73, 79, 72, 78, 75, 72, 74, 77, 70, 75, 79, 77, 76]

x = np.array(EN).reshape(-1, 1)
y = np.array(MATH)
print(x)
print(y)

from sklearn.linear_model import LinearRegression