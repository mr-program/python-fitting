'''
@Author: your name
@Date: 2020-03-28 13:16:07
@LastEditTime: 2020-04-02 08:58:22
@LastEditors: Please set LastEditors
@Description: 最小二乘拟合
@FilePath: \python-math\least_square_fitting.py
'''
import numpy as np
import math
from scipy import optimize


class Fitting:
    def __init__(self, x, y, type):
        self.X = np.array(x)
        self.Y = np.array(y)
        self.type = type
        
    # P是参数，X，Y是数据列表，type：拟合的次幂
    def residuals(self, p):
        if self.type == 1:
            K_1, b = p
            return self.Y - (K_1*self.X+b)
        elif self.type == 2:
            K_2, K_1, b = p
            return self.Y - (K_2*np.power(self.X,2)+K_1*self.X+b)
        elif self.type == 3:
            K_3, K_2, K_1, b = p
            return self.Y - (K_3*np.power(self.X,3)+K_2*np.power(self.X,2)+K_1*self.X+b)
        elif self.type == 4:
            K_4, K_3, K_2, K_1, b = p
            return self.Y - (K_4*np.power(self.X,4)+K_3*np.power(self.X,3)+K_2*np.power(self.X,2)+K_1*self.X+b)
        elif self.type == 5:
            K_5, K_4, K_3, K_2, K_1, b = p
            return self.Y -(K_5*np.power(self.X,5)+K_4*np.power(self.X,4)+K_3*np.power(self.X,3)+K_2*np.power(self.X,2)+K_1*self.X+b)
        else:
            pass

    def getAvgs(self):
        if self.type == 1:
            avgs = [1,0]
        elif self.type == 2:
            avgs = [1,1,0]
        elif self.type == 3:
            avgs = [1,1,1,0]
        elif self.type == 4:
            avgs = [1,1,1,1,0]
        elif self.type == 5:
            avgs = [1,1,1,1,1,0]
        else:
            pass
        r = optimize.leastsq(self.residuals, avgs)
        return r[0]