import numpy as np
import goujian
import shuru

num = len(shuru.jiedian_list)  # 结点数

K_list = []
for i in range(num):
    K_list.append([])
    for s in range(num):
        K_list[i].append(np.zeros((3, 3)))

for i in shuru.danyuan_list:
    K_list[i.dot_1][i.dot_1] = np.add(K_list[i.dot_1][i.dot_1], i.K_11)
    K_list[i.dot_1][i.dot_2] = np.add(K_list[i.dot_1][i.dot_2], i.K_12)
    K_list[i.dot_2][i.dot_1] = np.add(K_list[i.dot_2][i.dot_1], i.K_21)
    K_list[i.dot_2][i.dot_2] = np.add(K_list[i.dot_2][i.dot_2], i.K_22)

K = np.vstack([np.hstack(i) for i in K_list])  # 总体刚度矩阵

P_list = []
for i in range(num):
    P_list.append(np.zeros((3, 1)))

for i in shuru.danyuan_list:
    P_list[i.dot_1] = np.add(P_list[i.dot_1], i.P_1)
    P_list[i.dot_2] = np.add(P_list[i.dot_2], i.P_2)

P = np.vstack(P_list)  # 总体荷载

delta = np.dot(np.linalg.inv(K), P)  # 总体位移向量

