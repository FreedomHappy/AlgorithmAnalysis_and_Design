# encoding: utf-8
"""
@author: lin
@file: 最长公共子序列.py
@time: 2018/10/19 16:24
@desc:
"""

import numpy as np
"""
一、最优子结构
有两个序列X，Y
（1）Xm==Yn
    Z 为Xm-1和Yn-1的最长公共子序列
（2）Xm!=Yn
    1)Z 为Xm-1和Yn的最长公共子序列
    2)Z 为Xm和Yn-1的最长公共子序列
"""


# 计算公共子序列长度
def LCSLength(X, Y):
    c = np.zeros((len(X)+1, len(Y)+1))
    b = np.zeros((len(X)+1, len(Y)+1))
    for i in range(len(X)+1)[1:]:
        x = i - 1
        for j in range(len(Y)+1)[1:]:
            y = j - 1
            if X[x] == Y[y]:
                c[i][j] = c[i-1][j-1]+1
                b[i][j] = 1
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 3
    return c, b

# 找出公共最长子序列
def LCS(i, j, X, b):
    if i == 0 or j == 0:return
    if b[i][j] == 1:
        LCS(i-1, j-1, X, b)
        x = i-1
        print(X[x])
    elif b[i][j] == 2:
        LCS(i-1, j, X, b)
    else:
        LCS(i, j-1, X, b)

def main():
    A = ['A', 'C', 'G', 'T', 'T', 'C', 'G', 'A']
    B = ['C', 'G', 'A', 'T', 'T', 'C', 'G', 'G', 'A']
    c, b = LCSLength(A, B)
    print(c, '\n')
    print(b)
    print('A:', A)
    print('B:', B)
    LCS(len(A), len(B), A, b)

if __name__== "__main__":
    main()