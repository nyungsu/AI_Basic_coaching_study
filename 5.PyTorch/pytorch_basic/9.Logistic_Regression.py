import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1) #랜덤 선언할 때 시드 고정

x_data = [[1,2],
          [2,3],
          [3,1],
          [4,3],
          [5,3],
          [6,2]]

y_data =  [[0],
           [0],
           [0],
           [1],
           [1],
           [1]]

x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

w = torch.zeros((2,1), requires_grad=True)
b = torch.zeros((1,), requires_grad=True)

optimizer = optim.SGD([w,b], lr=1)

nb_epochs = 1000

for epoch in range(nb_epochs+1):
    hypothesis = torch.sigmoid(x_train.matmul(w)+b)
    
    # losses = -(y_train * torch.log(hypothesis) + 
    #            (1-y_train) * torch.log(1-hypothesis))
    # cost = losses.mean()
    cost = F.binary_cross_entropy(hypothesis,y_train)
    
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    
print(hypothesis)

print(cost)