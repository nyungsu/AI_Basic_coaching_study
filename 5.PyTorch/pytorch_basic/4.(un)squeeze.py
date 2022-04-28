import torch

a = torch.FloatTensor([[1],[2],[3]])
print(a)
print(a.shape)
print()
print(a.squeeze())
print(a.squeeze().shape)

# size = [3,1,20,128] tensor 생성
tensor = torch.rand(3,1,20,128)
print(tensor.shape)

# dim=1인 차원을 날려준다.
# dim을 설정 안 해주면 1인 차원 모두 날림
# 차원을 설정해주면 그 차원만 날림.
tensor = tensor.squeeze()
print(tensor.shape)

# 설정해준 차원에 1개 짜리 차원을 집어넣음.
tensor = tensor.unsqueeze(dim=1)
print(tensor.shape)





