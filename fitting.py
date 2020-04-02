'''
@Author: your name
@Date: 2020-04-02 08:51:24
@LastEditTime: 2020-04-02 13:35:24
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python-math\test.py
'''
from fitting_kernel import Fitting
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
from matplotlib.font_manager import FontProperties
import xlrd

# 打开excel，读取sheet0
excel = xlrd.open_workbook('fitting.xlsx', encoding_override='utf-8')
sheet = excel.sheets()[0]

# 读取基本信息
graph_name = sheet.cell_value(0,1)
type = sheet.cell_value(1,1)
data_step = sheet.cell_value(2,1)
x_disp_step = sheet.cell_value(3,1)
y_disp_step = sheet.cell_value(4,1)
x_label = sheet.cell_value(5,1)
y_label = sheet.cell_value(6,1)

# 获取x，y数据
x = sheet.col_values(0)
x = x[9:]
y = sheet.col_values(1)
y = y[9:]

# 获取x，y最大值和最小值
x_max = max(x)
x_min = min(x)
y_max = max(y)
y_min = min(y)

# 初始化拟合数据
x_test = np.arange(x_min, x_max, data_step)
y_test = np.arange(x_min, x_max, data_step)
label_function = ''

# 拟合曲线，返回参数
fit = Fitting(x,y,type)
if type ==1:
    K_1, b = fit.getAvgs()
    y_test = K_1*x_test+b
    label_function = '$y=('+str(K_1)+')*x+('+str(b)+')$'
elif type ==2:
    K_2, K_1, b = fit.getAvgs()
    y_test = K_2*np.power(x_test,2)+K_1*x_test+b
    label_function = '$y=('+str(K_2)+')*x^2+('+str(K_1)+')*x+('+str(b)+')$'
elif type ==3:
    K_3, K_2, K_1, b = fit.getAvgs()
    y_test = K_3*np.power(x_test,3)+K_2*np.power(x_test,2)+K_1*x_test+b
    label_function = '$y=('+str(K_3)+')*x^3+('+str(K_2)+')*x^2+('+str(K_1)+')*x+('+str(b)+')$'
elif type ==4:
    K_4, K_3, K_2, K_1, b = fit.getAvgs()
    y_test = K_4*np.power(x_test,4)+K_3*np.power(x_test,3)+K_2*np.power(x_test,2)+K_1*x_test+b
    label_function = '$y=('+str(K_4)+')*x^4+('+str(K_3)+')*x^3+('+str(K_2)+')*x^2+('+str(K_1)+')*x+('+str(b)+')$'
elif type ==5:
    K_5, K_4, K_3, K_2, K_1, b = fit.getAvgs()
    y_test = K_5*np.power(x_test,5)+K_4*np.power(x_test,4)+K_3*np.power(x_test,3)+K_2*np.power(x_test,2)+K_1*x_test+b
    label_function = '$y=('+str(K_5)+')*x^5+('+str(K_4)+')*x^4+('+str(K_3)+')*x^3+('+str(K_2)+')*x^2+('+str(K_1)+')*x+('+str(b)+')$'
else:
    pass

# 设定中文字体
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
# 设置图标标题
plt.title(graph_name, fontproperties=font)
# 绘制原始数据散点图
plt.scatter(np.array(x), np.array(y))
# 标注原始数据
for xy in zip(np.array(x), np.array(y)):
    plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-20, 10), textcoords='offset points')
# 绘制拟合后的数据曲线
plt.plot(x_test,y_test,label=label_function)
plt.xlabel(x_label, fontproperties=font)
plt.ylabel(y_label, fontproperties=font)
# 设置显示精度
x_major_locator=MultipleLocator(x_disp_step)
y_major_locator=MultipleLocator(y_disp_step)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
# 展示网格线并显示图标
plt.grid(True)
plt.legend()#显示图示
plt.show()
