import pandas as pd

# 3.딕트로 데이터 프레임 만들기
friend_dict_list = [
    {'name' : 'john', 'age': 26, 'job' : 'student'},
    {'name' : 'song', 'age' : 26, 'job' : 'public'}     
    ]

df3 = pd.DataFrame(friend_dict_list)
print(df3)

# 4.리스트로 데이터 프레임 만들기
friend_list = [
    ['jeong',30,'student'],
    ['song',26,'public'],
    ['lee',10,'student']    
]

df4 = pd.DataFrame(friend_list,columns=['name','age','job'])
print(df4)
