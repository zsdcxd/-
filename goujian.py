import numpy as np
import math
import tools


class danyuan(object):  # 单元分析
    def __init__(self, l, EI, EA=0, a=0, F_1=np.zeros((3, 1)), F_2=np.zeros((3, 1)), dot_1=None, dot_2=None):
        self.l = l
        self.dot_1 = dot_1
        self.dot_2 = dot_2
        self.EI = EI
        self.EA = EA
        self.i = self.EI / self.l

        self.K_0 = np.array([[self.EA / self.l, 0, 0, -self.EA / self.l, 0, 0],
                             [0, 12 * self.i / self.l ** 2, 6 * self.i / self.l, 0, -12 * self.i / self.l ** 2,
                              6 * self.i / self.l],
                             [0, 6 * self.i / self.l, 4 * self.i, 0, -6 * self.i / self.l, 2 * self.i],
                             [-self.EA / self.l, 0, 0, self.EA / self.l, 0, 0],
                             [0, -12 * self.i / self.l ** 2, -6 * self.i / self.l, 0, 12 * self.i / self.l ** 2,
                              -6 * self.i / self.l],
                             [0, 6 * self.i / self.l, 2 * self.i, 0, -6 * self.i / self.l, 4 * self.i]])  # 单元刚度矩阵

        if a != 0:
            self.T = np.array([[math.sqrt(1 - math.sin(math.radians(a)) ** 2), math.sin(math.radians(a)), 0, 0, 0, 0],
                               [-math.sin(math.radians(a)), math.sqrt(1 - math.sin(math.radians(a)) ** 2), 0, 0, 0, 0],
                               [0, 0, 1, 0, 0, 0],
                               [0, 0, 0, math.sqrt(1 - math.sin(math.radians(a)) ** 2), math.sin(math.radians(a)), 0],
                               [0, 0, 0, -math.sin(math.radians(a)), math.sqrt(1 - math.sin(math.radians(a)) ** 2), 0],
                               [0, 0, 0, 0, 0, 1]])  # 坐标转换矩阵，其中a为角度制角度

            self.K = np.dot(np.dot(tools.trans(self.T), self.K_0), self.T)  # 单元整体单刚
        else:
            self.K = self.K_0
        self.K_11 = self.K[0:3, 0:3]
        self.k_12 = self.K[0:3, 3:6]
        self.k_21 = self.K[3:6, 0:3]
        self.k_22 = self.K[3:6, 3:6]

        self.F_1 = F_1
        self.F_2 = F_2
        if np.any(F_1 != 0) or np.any(F_2 != 0) and a != 0:  # 判断是否有荷载
            self.lam = self.T[0:3, 0:3]
            self.P_1 = -np.dot(tools.trans(self.lam), self.F_1)
            self.P_2 = -np.dot(tools.trans(self.lam), self.F_2)
        else:
            self.P_1 = F_1
            self.P_2 = F_2

# ceshi= danyuan(12,144,6,None,None,90)
# print(ceshi.K)
