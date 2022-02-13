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
df2 = pd.DataFrame(data2)                       # 데이터 프레임 선언

df3 = pd.concat([df1,df2], axis=0)              # concat 함수로 df1 df2 붙임

# # 답지는 loc으로 접근
# df_fruit1 = df3.loc[df3['Type']=="Fruit"]
# df_veg = df3.loc[df3['Type']=="vegetable"]

df4 = df3.groupby('Type')                       # groupby함수를 이용해 type을 기준으로 찢음
for name,group in df4:
    if name =='Fruit':
        df_fruit2=group
    elif name =='Vegetable':
        df_vegetable=group

df_fruit2.sort_values(by=['Price'],inplace=True,ascending=False)        # inplace를 true 안 해주면 기존 데이터가 변경 되지 않고 이 줄에서만 변경
df_vegetable.sort_values(by=['Price'],inplace=True,ascending=False)     # sort_values 함수에서 ascending을 false 해주면 내림차순

fruit_top2 = df_fruit2['Price'].head(2).sum()                           # 내림차순으로 정렬된 상태에서 맨위 두줄은 top2
vegatable_top2 = df_vegetable['Price'].head(2).sum()

print(f'Sum of Top 2 Fruit Price : {fruit_top2}')
print(f'Sum of Top 2 Vegetable Price : {vegatable_top2}')





