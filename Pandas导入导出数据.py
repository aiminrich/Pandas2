'''如何在Pandas中储存或调用已经存储好的数据'''
import pandas as pd
import numpy as np
'''pandas库可以读取文件格式：
1.read_csv
2.read_excel
3.read_hdf
4.read_sql
5.read_json
6.read_msgpack
7.read_html
8.read_gbq
9.read_stata
10.read_sas
11.read_clipboard
12.read_pickle
'''

'''
Pandas保存文件：
1.to_csv
2.to_excel
3.to_sql
4.to_json
5.to_msgpack
6.to_html
7.to_gbp
8.to_stata
9.to_clipboard
10.to_pickle
'''
data = pd.read_csv('student.csv')        #读取一个后缀名为csv的表格文件
print('data为：\n',data)
#存储
data.to_pickle('student.pickle')          #把data存储为一个后缀名为pickle的文件，名为student.pickle
