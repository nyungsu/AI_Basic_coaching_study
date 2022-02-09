import pandas as pd
import os


# 1.경로 설정해서 파일 불러오기
path = os.getcwd()
print(f'현재 경로 : {path}')

df1 = pd.read_csv('practice_pandas\data.csv')
print(df1)
print()
print(df1.head(3))

# 2.read_csv 함수의 파라미터 
df2 = pd.read_csv('practice_pandas\data_no_head_tab.txt',
                  delimiter='\t',
                  header = None,
                  names=['성','이름','나이','전공','사는 곳'])
print(df2)