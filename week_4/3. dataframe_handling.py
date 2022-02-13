import pandas as pd

idx = ['Sue','Ryan','Jay','Jane','Anna']
col = ['round_1','round_2','round_3','round_4','round_5',]
data =[[55,65,60,66,57],
       [64,77,71,79,67],
       [88,81,79,89,77],
       [45,35,30,46,47],
       [91,96,90,97,99]]

df = pd.DataFrame(data=data,
                  columns=col,
                  index=idx)

df['round_6'] = [11,15,13,17,19]
print(df)

mean =[df[col].mean() for col in df.columns]            # list comprehesion을 이용하여 mean,max,min 출력
max = [df[col].max() for col in df.columns]
min = [df[col].min() for col in df.columns]

print('mean :',mean)
print('max :' ,max)
print('min :' ,min)

# 정답 예시코드에는 describe 함수 사용
print(df.describe().loc[['mean','max','min']])

'''
describe() : 통계량을 요약해주는 메소드
pandas의 dataframe의 경우 열에 대해 정보 요약이 가능
count, 갯수
mean, 평균
std, 표준편차
min , 최소값
25%
50%
75%
max, 최대값
'''

