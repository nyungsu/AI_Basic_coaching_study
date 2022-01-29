import numpy as np

xy = np.array([[1., 2., 3., 4., 5., 6.],
               [3.,6.,9.,12.,15.,18.]])

x_train = xy[0]
y_train = xy[1]

beta_gd = np.random.rand(1)
bias = np.random.rand(1)

learning_rate = 0.001

for i in range(1000):
    pred = (x_train * beta_gd) + bias
    error_MSE = ((pred - y_train)**2).mean()

    gd_w = ((pred - y_train) * 2 * x_train).mean()
    gd_b = ((pred - y_train) * 2 ).mean()

    beta_gd -= learning_rate *gd_w
    bias -= learning_rate *gd_b

    if i %100 ==0:
        print(f'epoch :{i}, error :{error_MSE}, weight :{beta_gd}, bias :{bias}')

