import pandas as pd
import numpy as np

left = pd.DataFrame({'key':['k0','k1','k2','k3'],
                                   'A':['A0','A1','A2','A3'],
                                   'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['k0','k1','k2','k3'],
                                     'C':['C0','C1','C2','C3'],
                                      'D':['D0','D1','D2','D3']})
print('left为：\n',left)
print('right为：\n',right)
res = pd.merge(left,right,on='key')            #第1，2个参数为要合并的DataFrame，on表示基于哪个column进行合并
print('res为：\n',res)

#如果有两个key
left1 = pd.DataFrame({'key1':['k0','k0','k1','k2'],
                                   'key2':['k0','k1','k0','k1'],
                                   'A':['A0','A1','A2','A3'],
                                   'B':['B0','B1','B2','B3']})
right1 = pd.DataFrame({'key1':['k0','k1','k1','k2'],
                                     'key2':['k0','k0','k0','k0'],
                                     'C':['C0','C1','C2','C3'],
                                      'D':['D0','D1','D2','D3']})
print('left1为：\n',left1)
print('right1为：\n',right1)
res1 = pd.merge(left1,right1,on=['key1','key2'],how='inner')   #默认的合并方法是inner
print('res1为：\n',res1)
'''
how = ['left','right','inner','outer']
1.'left'：基于left这个DataFrame的key把他合并下来
2.‘right’：基于right这个DataFrame的key来把他合并下来
3.‘outer’：不管这几个DataFrame一不一样，都把他复制下来，没有的地方为nan
4.'inner'：只复制一样的部分,考虑相同的KEY
'''
#indicator
df1 = pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print('df1为：\n',df1)
print('df2为：\n',df2)
res2 = pd.merge(df1,df2,on='col1',how='outer',indicator=True)
print('res2为：\n',res2)

#index
left2 = pd.DataFrame({'A':['A0','A1','A2'],
                                     'B':['B0','B1','B2'],},index=['k0','k1','k2'])
right2 = pd.DataFrame({'C':['C0','C2','C3'],
                                       'D':['D0','D2','D3']},index=['k0','k2','k3'])
print('--------------------------------------')
print('left2为：\n',left2)
print('--------------------------------------')
print('right2为：\n',right2)
res3 = pd.merge(left2,right2,left_index=True,right_index=True,how = 'outer')
print('-------------------------------------')
print('res3结果为：\n',res3)

#handle overlaping
boys = pd.DataFrame({'k':['k0','k1','k2'],
                                     'age':[1,2,3]})
girls = pd.DataFrame({'k':['k0','k0','k3'],
                                      'age':[4,5,6]})
print('--------------------------------------')
print('boys为：\n',boys)
print('--------------------------------------')
print('girls为：\n',girls)
res4 = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')
print('----------------------------------------')
print('res4为：\n',res4)
