import numpy as np
import pandas as pd

dates = pd.date_range('20220523',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print('df为：\n',df)
#把丢失的数据按行操作或列操作丢掉：dropna
# df = df.dropna(axis=1,how='any')   #how = 'any'  'all'，how=all时，只有在这一行（列）中所有全部为0时，才会把他丢掉，axis=0时，纵向操作，axis=1时，横向操作
# print('-----------------------------------------')
# print('current df 为：\n',df)

#把丢失的数据填上：fillna
df = df.fillna(value=0)
print('----------------------------------------------')
print('current df 为：\n',df)

#检查有没有数据：isnull
print('-----------------------------------------------')
print(df.isnull())

#表格很大看不清时：np.any
print('---------------------------------------------')
print(np.any(df.isnull()) == True)
