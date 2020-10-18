import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#matplotlib
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
data=pd.read_csv('zhai.csv')

# plt.boxplot(data)    				#垂直显示箱线图
# plt.boxplot(data,vert = False)    		#水平显示箱线图
# data.boxplot()  #对数据框中每列画箱线图
# plt.title('箱线图')

data['左肩'].plot()    #折线图
plt.title('left shoulder')

# data.plot.bar()   #垂直柱状图
# data.plot.barh()   #水平柱状图
# plt.title('柱状图')

# data.plot.barh(stacked=True, alpha = 0.5)    #堆积柱状图
# plt.title('堆积柱状图')

# data.plot.hist(bins=50)         #直方图
# plt.title('直方图')
# plt.savefig('12.jpg')     #保存图像
plt.show()