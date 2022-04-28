import pandas as pd
import numpy as np
# 1.groupby
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df1 = pd.DataFrame(ipl_data)
print(df1)

g_df1 = df1.groupby(['Team','Year'])['Points'].sum()

# 2. unstack()
print(g_df1['Devils':'Riders'])
print(g_df1['Devils':'Riders'].unstack())


# 3. grouped

for name,group in df1.groupby('Team'):
    print()
    print(name)
    print(group)
    
print(df1.groupby('Team').get_group('Devils'))

# 4. aggregation
print(df1.groupby('Team').agg(sum))
print(df1.groupby('Team')['Points'].agg([sum,np.mean,np.std]))