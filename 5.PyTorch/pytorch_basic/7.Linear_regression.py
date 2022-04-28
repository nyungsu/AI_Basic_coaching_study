import torch

x_train = torch.FloatTensor([[1],[2],[3]])
y_train = torch.FloatTensor([[2],[4],[6]])

w = torch.zeros(1, requires_grad=True)      # 값이 변경되는 변수라는 의미
b = torch.zeros(1, requires_grad=True)      # 값이 변경되는 변수라는 의미

optimizer = torch.optim.SGD([w,b],lr=0.01)

nb_epochs = 1000
for epoch in range(1,nb_epochs,1):
    #h(x) 계산
    hypothesis = x_train * w +b
    
    #cost 계산
    cost = torch.mean((hypothesis - y_train)**2)

    optimizer.zero_grad()       # 그래디언트 초기화
    cost.backward()             # 그래디언트 계산
    optimizer.step()            # w,b 스탭별로 업데이트
    
    
print(w,b)

