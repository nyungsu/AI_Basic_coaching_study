import pandas as pd

# 5.행 다루기
friend_list = [
    ['jeong',30,'student'],
    ['song',26,'public'],
    ['lee',10,'student']    
]
df5 = pd.DataFrame(friend_list,columns=['name','age','job'])
print(df5[1:3])         # 행 슬라이싱
print(df5.loc[0:2])     # 0~2까지
print(df5.loc[[0,2]])   # 0이랑 2는 [] 두 개

# 6.열 다루기
print(df5[df5.age>20])  # 조건 주기
print(df5[(df5.age>25) & (df5.name == 'song')])

print(df5.iloc[0:2,1:2])    # 0이상 2미만 행/ 1이상 2 미만 열
print(df5.loc[0:2,'age'])   # 0이상 2미만 행/ age 열

print(df5[['age','job']].iloc[0:2])   # 열 추출 [[]] 두 개 이상은 괄호 두 개

# 7. 행 열 지우기
print(df5.drop(1,inplace=True))   # 행 인덱스로 지우기
print(df5.drop('age', axis=1))    # 열 지우기
del df5['age']                    # 열 지우기

print(df5)

# 8.열 생성 및 추가
friend_list = [
    {'name' : 'jeong', 'mid' : 50, 'final' : 10},
    {'name' : 'lee', 'mid' : 40, 'final' : 20},
    {'name' : 'song', 'mid' : 30, 'final' : 20},
    {'name' : 'nam', 'mid' : 20, 'final' : 40},
    {'name' : 'choi', 'mid' : 10, 'final' : 40}]
df7 = pd.DataFrame(friend_list)

df7['total'] = df7.mid+df7.final
df7['mean'] = df7.total/2

grade =[]
for row in df7['mean']:
    if row >=27:
        grade.append('pass')
    else :
        grade.append('non-pass')

df7['grade'] = grade
    
print(df7)

# 10.행 생성 및 수정
friend_list = [
    {'name' : 'jeong', 'mid' : 50, 'final' : 10},
    {'name' : 'lee', 'mid' : 40, 'final' : 20},
    {'name' : 'song', 'mid' : 30, 'final' : 20},
    {'name' : 'nam', 'mid' : 20, 'final' : 40},
    {'name' : 'choi', 'mid' : 10, 'final' : 40}]
df10 = pd.DataFrame(friend_list)

new_data = [
    {'name' : 'kang', 'mid' : 50, 'final': 90}
]
df11=pd.DataFrame(new_data)

df10 = df10.append(df11,ignore_index=True)

print(df10)