import torch

a = torch.FloatTensor([[1,2],[3,4]])
b = torch.FloatTensor([[1],[2]])

print(a,a.shape)
print(b,b.shape)
print('--------------------------------')

#matmul 행렬 곱
matmul = torch.matmul(a,b)

#mul 그냥 곱
mul = torch.mul(a,b)

print(matmul,matmul.shape)
print(mul,mul.shape)