import torch
import numpy as np

tensor1 = torch.randint(0,20,size =(2,2))
tensor2 = torch.randint(0,20,size =(2,2))

matrix1 = np.random.randint(0,20,size=(2,2))
matrix2 = np.random.randint(0,20,size=(2,2))


torch_cat = torch.cat([tensor1,tensor2], dim=1)
print(torch_cat)

numpy_cat = np.concatenate((matrix1,matrix2),axis=0)
print(numpy_cat)




