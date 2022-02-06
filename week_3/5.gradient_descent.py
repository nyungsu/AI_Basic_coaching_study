import numpy as np

xy = np.array([[1., 2., 3., 4., 5., 6.],
               [3.,6.,9.,12.,15.,18.]])

x_train = xy[0]
y_train = xy[1]

beta_gd = np.random.rand(1)
bias = np.random.rand(1)

learning_rate = 0.001

for i in range(1000):
    pred = (x_train * beta_gd) + bias                       # np.random을 이용하여 뽑은 계수들로 임의의 선 하나 그음
    error_MSE = ((y_train - pred)**2).mean()                # pred 함수의 x에 x_train에 해당하는 값을 대입한 예측값과
                                                            # 실제 y_train 값들의 오차를 mean 

    gd_w = ((pred - y_train) * 2 * x_train).mean()          # W변수로 편미분 한 값, 합성함수의 미분(wx)'=x 곱해짐
    gd_b = ((pred - y_train) * 2 ).mean()                   # b변수로 편미분 한 값, 합성함수의 미분 (b)'=1 곱해짐

    beta_gd -= learning_rate *gd_w                          # 경사하강법,
    bias -= learning_rate *gd_b                             # learning_rate, 미분값 이용하여 업데이트

    if i %100 ==0:
        print(f'epoch :{i}, error :{error_MSE}, weight :{beta_gd}, bias :{bias}')

