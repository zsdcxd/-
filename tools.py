import numpy as np
import math


def trans(l):  # 求矩阵转置
    l = zip(*l)
    l = np.array([list(i) for i in l])
    return l


def dist(a, b):  # 求两点距离
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def angle(a, b):  # 求杆的角度
    return math.degrees(math.atan2(a[1] - b[1], a[0] - b[0]))
