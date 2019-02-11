# encoding: utf-8
"""
@author: lin
@file: MinimumSpanningTree_Prim.py
@time: 2018/10/30 9:53
@desc:最小生成树使用Prim算法
"""

import numpy as np
import matplotlib.pyplot as plt

def prim(C):
    min_tree = []
    min_index = []
    first = 0   # 选取的初始节点的索引
    min_index.append(first)

    while 1:
        # 找出下一个的点
        min = np.inf
        for i in range(len(C)):
            if i not in min_index:
                for idx in min_index:
                    if min>C[i][idx]:
                        min = C[i][idx]
                        this = idx
                        next = i
        min_index.append(next)
        min_tree.append((this, next))
        if len(min_index)==len(C):
            break
    return min_index, min_tree


def main():
    node_num = 6
    edge_num = 10
    C = [[0, 6, 1, 5, np.inf, np.inf],
         [6, 0, 5, np.inf, 3, np.inf],
         [1, 5, 0, 5, 6, 4],
         [5, np.inf, 5, 0, np.inf, 2],
         [np.inf, 3, 6, np.inf, 0, 6],
         [np.inf, np.inf, 4, 2, 6, 0]]
    idx, tree = prim(C)
    print(idx)
    print(tree)
    sum_weight = 0
    for edge in tree:
        sum_weight += C[edge[0]][edge[1]]
    print(sum_weight)
if __name__=="__main__":
    main()