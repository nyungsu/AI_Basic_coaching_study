import torch
import numpy as np


a = torch.FloatTensor([[1,2,3],[4,5,6]])

print(a)
print('행렬 a')
print()

print(a.sum())
print('전체 sum')
print()

print(a.sum(dim=0))
print('dim 0 방향으로 sum')
print()

print(a.sum(dim=1))
print('dim 1 방향으로 sum')
print()

# mean도 똑같이 동작함@@@@@@@

# reshape = view
print(a.view([3,2]))
print(a.view([-1,1]))


matrix = np.random.randint(0,20, size=(4,4))
print(matrix)
print()

tensor = torch.tensor(matrix)
print(tensor)
print()

# 좌표로 안 주고 몇번째에 있는지 값을 반환
print(torch.argmax(tensor))

# 가장 큰 값이 뭔지 반환    
print(torch.max(tensor))
