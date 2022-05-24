import matplotlib_inline.backend_inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#plot data

'''
Series
'''
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
data.plot()


'''
DataFrame(Pandas库里面的，是一个类似矩阵的东西)
'''
data1 = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))
print(data1.head())   #data.head默认前五个数据
data1 = data1.cumsum()
data1.plot()


#plot methods
'''
1.Bar，条形图
2.hist
3.box
4.kde
5.area
6.scatter
7.hexbin
8.pie
'''
data2 = data1.plot.scatter(x = 'A',y = 'B',color = 'red',label = 'Class1')
data1.plot.scatter(x = 'A',y = 'C',color = 'pink',label = 'Class2',ax = data2)

plt.show()
