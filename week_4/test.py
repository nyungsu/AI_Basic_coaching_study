import pandas as pd


friend_list = [
    {'name' : 'jeong', 'mid' : 50, 'final' : 10},
    {'name' : 'lee', 'mid' : 40, 'final' : 20},
    {'name' : 'song', 'mid' : 30, 'final' : 20},
    {'name' : 'nam', 'mid' : 20, 'final' : 40},
    {'name' : 'choi', 'mid' : 10, 'final' : 40}]
df = pd.DataFrame(friend_list)

new_data = [
    {'name' : 'kang', 'mid' : 50, 'final': 90}
]
df2=pd.DataFrame(new_data)

df = df.append(df2,ignore_index=True)

print(df)
