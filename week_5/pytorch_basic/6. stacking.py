import torch

a = torch.tensor([[1,2,3],[4,5,6]])
b = torch.tensor([[4,5,6],[1,2,3]])

cat = torch.cat([a,b],dim=0)
print(cat.shape)

stack = torch.stack([a,b])
print(stack.shape)
