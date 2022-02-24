import torch
import torch.nn as nn
import torch.nn.functional as F 
import torch.optim as optim

import torchvision.datasets as dset 
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

# =================여기부터 2번 ========================

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
linear = nn.Linear(784,10,bias=True).to(device)
# 28*28 = 784 의 input, 0~9까지 10개의 output

nn.init.normal_(linear.weight)

# =================여기부터 3번 ========================

criterion = nn.CrossEntropyLoss().to(device)
optimizer = optim.SGD(linear.parameters(), lr=0.1)
# nn.Linear의 클래스에 .parameters() 메소드를 이용하면

print(list(linear.parameters()))