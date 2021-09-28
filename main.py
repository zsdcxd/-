import numpy as np
import math


class danyuan(object):#单元分析
    def __init__(self, l, EI, EA=0, P_1=None, P_2=None, a=0):
        self.l = l
        self.EI = EI
        self.EA = EA
        self.i = self.EI / self.l
        self.E = np.mat([[self.EA / self.l, 0, 0, -self.EA / self.l, 0, 0],
                         [0, 12 * self.i / self.l ** 2, 6 * self.i / self.l, 0, -12 * self.i / self.l ** 2,
                          6 * self.i / self.l],
                         [0, 6 * self.i / self.l, 4*self.i, 0, -6 * self.i / self.l, 2*self.i],
                         [-self.EA / self.l, 0, 0, self.EA / self.l, 0, 0],
                         [0, -12 * self.i / self.l ** 2, -6 * self.i / self.l, 0, 12 * self.i / self.l ** 2,
                          -6 * self.i / self.l],
                          [0, 6 * self.i / self.l, 2*self.i, 0, -6 * self.i / self.l, 4*self.i]])#单元刚度
        self.T = np.mat([[math.sqrt(1-math.sin(math.radians(a))**2),math.sin(math.radians(a)),0,0,0,0],
                         [-math.sin(math.radians(a)),math.sqrt(1-math.sin(math.radians(a))**2),0,0,0,0],
                         [0,0,1,0,0,0],
                         [0,0,0,math.sqrt(1-math.sin(math.radians(a))**2),math.sin(math.radians(a)),0],
                         [0,0,0,-math.sin(math.radians(a)),math.sqrt(1-math.sin(math.radians(a))**2),0],
                         [0,0,0,0,0,1]])#坐标转换矩阵，其中a为角度制角度



# ceshi= danyuan(1,0,0,0,0,0)
# print(ceshi.T)


