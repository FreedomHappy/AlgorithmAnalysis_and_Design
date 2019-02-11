# encoding: utf-8
"""
@author: lin
@file: 01bag_test.py
@time: 2018/12/5 21:00
@desc:
"""
# encoding: utf-8

import numpy as np
import queue
import math

def KnapsackProblem_test(capacity,w,v):# 背包容量
    vec_len = 2 ** (len(v) + 1) - 1  # tree `s size
    vec_v = np.zeros(vec_len)
    vec_w = np.zeros(vec_len)
    vec_w[0] = capacity
    que = queue.Queue()
    que.put(0) # 结点 index 0
    best = 0
    while (not que.empty()):# 非空则存在未探索解
        current = que.get()
        level = int(math.log(current + 1, 2))
        if (vec_v[current] > vec_v[best]):
            best = current
        # 检查扩展子结点
        left = 2 * current + 1  # left child index
        right = 2 * current + 2  # right child index
        # 左结点加上这个物体，满足结点index未超出范围，未超出背包承重，加上当前
        if (left < vec_len and vec_w[current] - w[level] >= 0 ):
                # and vec_v[current] + v[level] > vec_v[best]):
            vec_v[left] = (vec_v[current] + v[level])
            vec_w[left] = vec_w[current] - w[level]
            que.put(left)
        # 右结点，不加这个物体
        if (right < vec_len and sum(v[level + 1:-1]) + vec_v[current] > vec_v[best]):
            vec_v[right] = vec_v[current]
            vec_w[right] = vec_w[current]
            que.put(right)
    print(vec_w[best], vec_v[best])


if __name__ == '__main__':
    # w = [3, 5, 2, 1]  # weight
    # v = [9, 10, 0.5, 4]  # value
    # bug测试数据
    w = [4, 2, 1, 2]
    v = [10, 9, 0.5, 3]
    # KnapsackProblem_test(7,w,v)
    KnapsackProblem_test(5,w,v)