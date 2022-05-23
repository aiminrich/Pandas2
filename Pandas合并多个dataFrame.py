import pandas as pd
import numpy as np

#如何合并多个DataFrame：concatenating
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])     #参数是几行几列，要用括号括住
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
print('df1为：\n',df1)
print('df2为：\n',df2)
print('df3为：\n',df3)
#合并这三个DataFrame
res = pd.concat([df1,df2,df3],axis=0)           #把要合并的DataFrame放在一个列表中，axis=0是纵向处理，axis=1是横向处理
print('res为：\n',res)

#如何把合并后的索引的值变换递增的模式：ignore_index=True
res1 = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print('res1为：\n',res1)

#Method2：join，['inner','outer']
df4 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df5 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print('df4为：\n',df4)
print('df5为：\n',df5)
res2 = pd.concat([df4,df5],join='inner')   #join=outer时，输出的合并结果为把几个dataFrame没有的东西用nan代替
#join=inner时，输出的合并结果只考虑几个DataFrame共有的部分
print('res2为：\n',res2)

#处理以下合并以后的Index序号，与前面的方式一样，用：ignore_index
res3 = pd.concat([df4,df5],join='inner',ignore_index=True)
print('res3为：\n',res3)

#join_axes
#现在已经没有join_axes函数了！！！
'''df6 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df7 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print('df6为：\n',df6)
print('df7为：\n',df7)
res4 = pd.concat([df6,df7],axis=1,join_axes = [df6.index])
print('-----------------------------------------')
print('res4为：\n',res4)'''


#append添加
res5 = df1.append(df2,ignore_index=True)           #将df2的这一组数据加到df1中
print('res5为：\n',res5)

#append添加不止一个DataFrame
res6 = df1.append([df2,df3],ignore_index=True)    #把多个DataFrame放在一个列表中
print('res6为：\n',res6)

#一项一项的加：
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res7 = df1.append(s1,ignore_index=True)
print('res7为：\n',res7)
