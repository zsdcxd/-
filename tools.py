import numpy as np
def trans(l):   #求矩阵转置
    l = zip(*l)
    l = np.array([list(i) for i in l])
    return l