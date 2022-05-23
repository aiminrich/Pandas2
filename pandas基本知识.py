'''Numpy和Pandas的区别：
1.Numpy:相当于一个列表；Pandas相当于一个字典'''
import pandas as pd
import numpy as np

#如何创建一个序列
S = pd.Series([1,3,6,np.nan,44,1])   #结果自动添加了一个序号。
print('S is :\n',S)

#如何创建一个大的Dataform
dates = pd.date_range('20220523',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])   #行的索引为index,列的索引为colums
print(df)

#不定义行和列的名称，用默认的名称。默认为0开始的序列
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print('df1 is :\n',df1)

df2 = pd.DataFrame({'A':1.,
                                   'B':pd.Timestamp('20220523'),
                                   'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                                   'D':np.array([3]*4,dtype='int32'),
                                   'E':pd.Categorical(['test','train','test','train']),
                                   'F':'foo'})
print('df2为:\n',df2)
print(df2.dtypes)
print('df2的行序号为：\n',df2.index)
print('df2的列序号为:\n',df2.columns)
print('df2的值为:\n',df2.values)


#描述df2
print('df2的描述为:\n',df2.describe())        #describe只是描述数字形式的，平均值，方差，最小值，求和……

#排序_index
A = df2.sort_index(axis=1,ascending=False)     #axis=1按行排序，axis=0按列排序
print('A为：\n',A)
B = df2.sort_index(axis=0,ascending=False)
print('B为：\n',B)

#排序_value
C = df2.sort_values(by='E')
print('C为：\n',C)
