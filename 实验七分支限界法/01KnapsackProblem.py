# encoding: utf-8
"""
@author: lin
@file: 01KnapsackProblem.py
@time: 2018/12/5 15:21
@desc:
"""

import numpy as np
import queue
import math

def getAnswer(best,length):
    answer = []
    while True:
        if (best % 2 == 1):
            answer.append(1)
            best = best // 2
        else:
            answer.append(0)
            best = (best-1) // 2
        if(best==0):
            break
    rest = [0]*(length-len(answer))
    return answer[::-1]+rest
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
        if (vec_v[current] >= vec_v[best]):
            best = current
        # 检查扩展子结点
        left = 2 * current + 1  # left child index
        right = 2 * current + 2  # right child index
        # 左结点加上这个物体，满足结点index未超出范围，未超出背包承重，加上当前
        if (left < vec_len and vec_w[current] - w[level] >= 0 ):
            vec_v[left] = (vec_v[current] + v[level])
            vec_w[left] = vec_w[current] - w[level]
            que.put(left)
        # 右结点，不加这个物体
        if (right < vec_len and sum(v[level + 1:-1]) + vec_v[current] > vec_v[best]):
            vec_v[right] = vec_v[current]
            vec_w[right] = vec_w[current]
            que.put(right)
    print(getAnswer(best,len(v)), vec_v[best])

def main():
    w1 = [7, 13, 6, 4,3]
    v1 = [5, 7, 3, 2, 3]
    KnapsackProblem_test(20, w1, v1)
    w2 = [7,13,45,25,16,75,48,32]
    v2 = [6,5,20,10,7,32,22,13]
    KnapsackProblem_test(100, w2, v2)
if __name__ == '__main__':
   main()
