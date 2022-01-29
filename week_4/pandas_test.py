from ctypes.wintypes import SERVICE_STATUS_HANDLE
import pandas as pd
import numpy as np


# data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'

# df_data = pd.read_csv(data_url, sep = '\s+', header=None)

# df_data.columns = [
#     'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX',
#     'RM', 'AGE', 'DIS', 'RAD', 'TAX',
#     'PTRATIO' ,'B', 'LSTAT', 'MEDV']

# print(df_data.head())       # 처음 다섯줄 


# #시리즈 이해하기
# idx = [1,2,3,4,5]
# name = ['a','b','c','d','e']
# data_s = pd.Series(data = name, index=idx)

# print(data_s)

# data_s = pd.Series({1:'a', 2:'b', 3:'c', 4:'d'})
# print(data_s)


#데이터 프레임 이해하기
# raw_data = {'first_name': ['Jason', 'Molly', 'Tina'],
#     'last_name': ['Miller', 'Jacobson', 'Ali'],
#     'age': [42, 52, 36],
#     'city': ['San Francisco', 'Baltimore', 'Miami'],
#     'debt' : [np.nan,np.nan,np.nan]}

# data_df = pd.DataFrame(raw_data)
# print(data_df)
# print(data_df.first_name)
# print(data_df['first_name'])

# ex = pd.Series(data = np.nan, index = [44,45,1,2,3,4])
# print(ex)

# print(ex.loc[:3])       #index 이름 3까지
# print(ex.iloc[:3])      #index 번호 3번째까지


# raw_data = {'first_name': ['Jason', 'Molly', 'Tina'],
#     'last_name': ['Miller', 'Jacobson', 'Ali'],
#     'age': [42, 52, 36],
#     'city': ['San Francisco', 'Baltimore', 'Miami'],
#     'debt' : [np.nan,np.nan,np.nan]}

# data_df = pd.DataFrame(raw_data)

# data_df.debt = data_df.age>40

# data_df.debt[data_df.age>40] = 0
#ex['debt'][ex['age']>40] = 0  이 두 개 같은 의미

# print(data_df)


# raw_data = {'first_name': ['Jason', 'Molly', 'Tina'],
#      'last_name': ['Miller', 'Jacobson', 'Ali'],
#      'age': [42, 52, 36],
#      'city': ['San Francisco', 'Baltimore', 'Miami'],
#      'debt' : [np.nan,np.nan,np.nan]}

# ex = pd.DataFrame(raw_data)
# print(ex)


# print(ex['age']>40)

# ex['debt'][ex['age']>40] = 0 

# print(ex)

# raw_data = {'first_name': ['Jason', 'Molly', 'Tina'],
#      'last_name': ['Miller', 'Jacobson', 'Ali'],
#      'age': [42, 52, 36],
#      'city': ['San Francisco', 'Baltimore', 'Miami'],
#      'debt' : [np.nan,np.nan,np.nan]}

# ex = pd.DataFrame(raw_data)
# print(ex)

# print(ex['first_name'].head(2))

# print(ex['first_name'][[0,2]])

# ex.drop(2,inplace=True)

# ex.drop(1,inplace=True)

# del(ex['first_name'])

# print(ex)

# a = pd.Series(index=['a','b','c','d'],data=[1,2,3,4])
# b = pd.Series(index=['b','c','d','e'],data=[1,2,3,4])
# print(a)
# print(b)
# print(a+b)

index = [1,2,3,4,5]
data = ['a','b','c','d','e']
dict_data = {1:'a',2:'b',3:'c',4:'d',5:'e'}

# a = pd.Series(index=index, data = data)
# b = pd.Series(dict_data)
# print(a)
# print(b)



raw_data = {'first_name': ['Jason', 'Molly', 'Tina'],
    'last_name': ['Miller', 'Jacobson', 'Ali'],
    'age': [42, 52, 36],
    'city': ['San Francisco', 'Baltimore', 'Miami']}

data_df = pd.DataFrame(raw_data)
print(data_df)




