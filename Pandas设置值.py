#如何给选定的范围赋另一个值
import pandas as pd
import numpy as np

dates = pd.date_range('20220523',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print('df为：\n',df)
#改变df的值
#方法一：以position定位他(iloc)，再赋值
E = df.iloc[2,2] = 1111         #把df第二行第二列重新定义为1111
print('-----------------------------------')
print('current df为：\n',df)
#方法二：以label定位他(loc)，再赋值
F = df.loc['20220525','C'] = 222
print('---------------------------------------')
print('current df为：\n',df)
#方法三：选中一个范围赋值
# G = df[df.A>4] = 0                     #A这一列>4的，数把剩下的这几行都赋值为0
# print('---------------------------------------')
# print('current df为：\n',df)

#只将A这一列>4的位置赋值为0，别的列不变
H = df.A[df.A>4] = 520
print('------------------------------------------')
print('current df为：\n',df)

#在df中加一列E赋值给df1
df['E'] =np.nan
print('-----------------------------------------')
print('当前df为：\n',df)

#加一个不为0的列
df['F'] = np.arange(1,7)
print('---------------------------------------')
print('current df 为：\n',df)
