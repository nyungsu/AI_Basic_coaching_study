import pandas as pd

idx = ['HDD','SSD','USB','CLOUD']
data = [19,11,5,97]

s = pd.Series(index=idx,data=data)
print(s)

s = s[(s>=10) & (s<=20)]
print(s)


'''
답안 예시에는 이렇게 했음
s = s[s>=10][s<=20]
'''


