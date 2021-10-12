import numpy as np

x = [-4, -3, 14, 8, 1, -5, -7, -4, -2, 6, 10, 22, 15, -15, -20]

def linear_prediction(p = 2):
    # 4.3.1
    Y = np.array(x[p:])
    X = []
    for i in range(len(x)-p):
        X_list = []
        for j in range(p-1, -1, -1):
          X_list.append(x[i+j])
        
        X.append(X_list)
    X = np.array(X).T
    print("X:\n", X)
    print("\nY:\n", Y)
    Rxx = X@X.T/len(Y)
    INV_Rxx = np.linalg.inv(Rxx)
    print("\nRxx:\n", Rxx)
    rxy = X@Y/len(Y)
    print("\nrxy:\n", rxy)
    
    # 4.3.2 예측 파라미터 구하기
    optimal_param = INV_Rxx@rxy
    print("\n예측기 파라미터 세타:\n", optimal_param)
    
    # 4.3.2 x15값 예측하기
    predict_list = []
    for i in range(p):
        predict_list.append([x[-1-i]])
    predict_list = np.array(predict_list)
    x_15 = optimal_param@predict_list
    print("\nx_15예측값:\n", x_15)
    
    # 4.3.3 MSE 평균 제곱 오차 구하기
    MSE = 0;
    error = [];
    for i in range(0, len(Y)):
        X_list = []
        for j in range(p):
            X_list.append(X[j][i])
        X_list = np.array(X_list)
        error.append(optimal_param@X_list)
    for i in range(len(error)):
        MSE += (x[i+p] - error[i])**2
        
    print("\n 오차 리스트:\n", error)
    print("\nMSE: \n", MSE/len(Y))
    print("-------------------p = {} case end------------------\n".format(p))
    
linear_prediction()
linear_prediction(4)