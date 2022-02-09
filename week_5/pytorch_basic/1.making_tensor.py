import torch

v = torch.FloatTensor([1,2,3])
m = torch.FloatTensor([[1,2,3],[4,5,6]])
t = torch.FloatTensor([[[1,2,3],[4,5,6],[7,8,9]],
                       [[1,2,3],[4,5,6],[7,8,9]],
                       [[1,2,3],[4,5,6],[7,8,9]],])

print(v)
print(v.shape)
print(v.ndim)
print()

print(m)
print(m.shape)
print(m.ndim)
print()

print(t)
print(t.shape)
print(t.ndim)

