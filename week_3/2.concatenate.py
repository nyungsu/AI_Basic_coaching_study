

import numpy as np

arr1 = np.array([[5,7],[9,11]])
arr2 = np.array([[2,4],[6,8]])

concat_0 = np.concatenate((arr1,arr2),axis=0,dtype=float)
concat_1 = np.concatenate((arr1,arr2),axis=1,dtype=float)

print(concat_0)
print(concat_1)



'''
concatenate axis 설정할 때
shape로 생각하자
예를 들어서

vector = np.array([1,2])
matrix = np.array([[1,2],[3,4]])
tensor = np.array([[[1,2,3],[4,5,6],[7,8,9]],
                   [[1,2,3],[4,5,6],[7,8,9]],
                   [[1,2,3],[4,5,6],[7,8,9]]])
print(vector.shape) (2,)        
print(matrix.shape) (2, 2)      
print(tensor.shape) (3, 3, 3)
axis=뒤에 숫자는 shape 순으로 있는 차원 방향으로 생각하면 됨
'''
