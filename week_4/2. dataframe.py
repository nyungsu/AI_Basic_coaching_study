'''
막 concat을 끝낸 df3와
groupby로 나눈 df_fruit,df_vegetable 두 개의 타입을 찍어보면
<class 'pandas.core.frame.DataFrame'>
똑같이 dataframe 클래스라고 뜨는데
concat을 끝낸 df3는 .sort_values 함수가 먹히고
df_fruit는 .sort_values 함수가 안 먹히네
왜 이럴까?
여튼 그래서 groupby 넣기전에 내림차순으로 정리하고 
groupby에 넣으니까 정렬 되어서 나오길래
정렬하고 groupby로 나누었다.
'''

import pandas as pd

data1 = [
    {'Name' : 'cherry', 'Type' : 'Fruit', 'Price':100},
    {'Name' : 'mango', 'Type' : 'Fruit', 'Price':110},
    {'Name' : 'potato', 'Type' : 'Vegetable', 'Price':60},
    {'Name' : 'onion', 'Type' : 'Vegetable', 'Price':80}
        ]

data2 = [
    {'Name' : 'pepper', 'Type' : 'Vegetable', 'Price':50},
    {'Name' : 'carrot', 'Type' : 'Vegetable', 'Price':70},
    {'Name' : 'banana', 'Type' : 'Fruit', 'Price':90},
    {'Name' : 'kiwi', 'Type' : 'Fruit', 'Price':120}
        ]

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df3 = pd.concat([df1,df2])
df3.sort_values(by=['Price'],inplace=True,ascending=False)
# df3에서는 sort가 먹히는데,
# 아래에 groupby 하고 나면 .sort가 안 먹혀서
# 내림차순으로 정렬하고 groupby로 나누었다.

df4 = df3.groupby('Type')
for name,group in df4:
    if name =='Fruit':
        df_fruit=group
    elif name =='Vegetable':
        df_vegetable=group

fruit_top2 = df_fruit['Price'].head(2).sum()
vegatable_top2 = df_vegetable['Price'].head(2).sum()

print(f'Sum of Top 2 Fruit Price : {fruit_top2}')
print(f'Sum of Top 2 Vegetable Price : {vegatable_top2}')





