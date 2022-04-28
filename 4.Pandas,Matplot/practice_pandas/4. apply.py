import pandas as pd

# 9.apply
data_list = [
    {'yyyy-mm-dd' : '1997-11-28'},
    {'yyyy-mm-dd' : '1997-02-15'},
    {'yyyy-mm-dd' : '1997-03-20'},
    {'yyyy-mm-dd' : '2000-09-29'},
    {'yyyy-mm-dd' : '1962-11-03'},
    {'yyyy-mm-dd' : '1964-02-26'}
]

df9 = pd.DataFrame(data_list,
                  columns=['yyyy-mm-dd'])
print(df9)

def extract_year(row):
    return row.split('-')[0]

def extract_month(row):
    return row.split('-')[1]

def extract_day(row):
    return row.split('-')[2]

df9['year'] = df9['yyyy-mm-dd'].apply(extract_year)
df9['month'] = df9['yyyy-mm-dd'].apply(extract_month)
df9['day'] = df9['yyyy-mm-dd'].apply(extract_day)

df9.drop('yyyy-mm-dd',axis=1,inplace=True)
print(df9)