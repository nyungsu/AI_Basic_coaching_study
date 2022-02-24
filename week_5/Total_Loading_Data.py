import torch
import torch.nn as nn
import torch.nn.functional as F 
import torch.optim as optim

import torchvision.datasets as dset 
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

training_epochs = 15
batch_size = 100

root = "./week_5/data"

# pytorch의 datasets 패키지에서 MNIST 데이터를 지정한 경로에 다운
mnist_train = dset.MNIST(root=root,
                         train=True,          # true 하면 train_set
                         transform=transforms.ToTensor(),
                         download=True)       # 없으면 다운 받겠다

mnist_test = dset.MNIST(root=root,
                        train=False,         # False 하면 test_set
                        transform=transforms.ToTensor(),
                        download=True)       

# 다운 받은 데이터 셋을 이용하기 위해
# DataLoader라는 클래스를 이용
train_loader = DataLoader(dataset=mnist_train,
                          batch_size = batch_size, 
                          shuffle=True, 
                          drop_last=True)           
                                                  
test_loader = DataLoader(dataset=mnist_test,   
                          batch_size = batch_size, 
                          shuffle=True,           
                          drop_last=True)

# =================여기부터 2번 ========================
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
linear = nn.Linear(784,10,bias=True).to(device)
# 28*28 = 784 의 input, 0~9까지 10개의 output
# to(device)는 문법을 보면
# gpu가 있으면 gpu를 쓰고 없으면 cpu 쓰라는 뜻 같다
# .to(device)다 날리고 써봤는데 동작 되더라

nn.init.normal_(linear.weight)

# =================여기부터 3번 ========================

criterion = nn.CrossEntropyLoss().to(device)
optimizer = optim.SGD(linear.parameters(), lr=0.1)
# nn.Linear의 클래스에 .parameters() 메소드를 이용하면
# 모델의 파라미터를 받을 수 있다.
# 제너레이터로 저장 되어있음

# =================여기부터 4번 ====================

for epoch in range(training_epochs):
    # 600장의 train 데이터
    # batch size = 100이라
    # 6번 돌면 1epoch
    # 이 밑에 for문에서는 6번의 이터레이션이 돈다
    for batch_idx, (imgs, labels) in enumerate(train_loader):
        imgs, labels = imgs.to(device), labels.to(device)
        imgs = imgs.view(-1,28*28)
        
        outputs = linear(imgs)
        loss = criterion(outputs, labels)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        _,argmax = torch.max(outputs, 1)
        accuracy = (labels == argmax).float().mean()

        if (batch_idx+1) % 100 ==0:
            print(f'epoch : {epoch+1}/{training_epochs}')
            print(f'batch : {batch_idx+1}/{len(train_loader)}')
            print(f'loss : {loss}')
            print(f'accuracy : {accuracy}')
            print()
       
# =================여기서부터 5번 ==========================       
            
with torch.no_grad():
    correct = 0
    total =0
    for i, (imgs,labels) in enumerate(test_loader):
        imgs, labels = imgs.to(device), labels.to(device)
        imgs = imgs.view(-1,28*28)
        outputs = linear(imgs)
        _, argmax = torch.mas(outputs,1)
        total += imgs.size(0)
        correct += (labels == argmax).sum().items()
        
    print('test accuracy for {total} imges : {correct}')