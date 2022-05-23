import numpy as np
import pandas as pd

dates = pd.date_range('20220523',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print('df为：\n',df)

#选择A、B、C、D的某一列
E = df['A']
print('E为：\n',E)
F = df.A
print('F为：\n',F)

#按照切片进行选择
G = df[0:3],df['20220523':'20220525']
print('G为：\n',G)

#高级选法——选横向标签
H = df.loc['20220523']
print('-----------------------------------')
print('H为:\n',H)

#高级选法——选纵向标签
I = df.loc[:,['A','B']]
print('-----------------------------------')
print('I为：\n',I)

#高级选法——都选
J = df.loc['20220523',['A','B']]
print('------------------------------------')
print('J为：\n',J)

#select by position ：iloc
K = df.iloc[3:5,1:3]          #第一个参数表示第几行，第二个参数表示第几位
print('K为：\n',K)

#一个一个筛选
L = df.iloc[[1,3,5],1:3]             #第一个参数表示筛选第1，3，5行，第二个参数表示筛选第1到第3列
print('-------------------------------')
print('L为：\n',L)

# #将label(loc)和position(iloc)合并起来一起筛选：mixed selection:ix
# M = df.ix[:3,['A','C']]
# print('M为：\n',M)
'''ix 版本已经被弃用了！！！'''

#进行是或否的筛选
M = df[df.A>8]
print('----------------------------')
print('M为：',M)           #筛选的是整套的数据
