import pandas as pd

idx = ['HDD','SSD','USB','CLOUD']
data = [19,11,5,97]

s = pd.Series(index=idx,data=data)
print(s)

s = s[(s>=10) &(s<=20)]
print(s)

'''
s안에 data 값이 10 이상 20이하길래
처음에는 s[data>=10] 이런식으로 접근했음
데이터 프레임이면 저렇게 인덱스르 줘야겠지만
시리즈는 한 줄 이기 때문에 저런듯
'''

