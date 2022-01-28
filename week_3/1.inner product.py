import numpy as np

arr1 = np.random.randint(0,10,(5,3))
arr2 = np.random.randint(0,10,(3,2))

print(arr1, f', shape :{arr1.shape}')
print(arr2, f', shape :{arr2.shape}')

# @연산자 사용 , np.matmul()랑 같다고 함
at_mul = arr1@arr2
print(at_mul, at_mul.shape)

# np.dot() 사용
np_dot_mul = np.dot(arr1,arr2)
print(np_dot_mul,np_dot_mul.shape)




# # 2차원 배열에서는 np.matmul()과 np.dot() 같음
# # -----------------------------------------------
# arr3 = np.random.randint(0,10,(2,3,3))
# arr4 = np.random.randint(0,10,(2,3,3))
# print(arr3, f', shape :{arr3.shape}')
# print(arr4, f', shape :{arr4.shape}')

# at_mul = arr3@arr4 # np.matmul()이랑 같음
# print(at_mul, f', shape :{at_mul.shape}')

# np_dot_mul = np.dot(arr3,arr4)
# print(np_dot_mul, f', shape :{np_dot_mul.shape}')
# # 3차원 부터는 다르게 동작
