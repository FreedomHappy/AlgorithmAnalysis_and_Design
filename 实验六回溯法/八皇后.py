# encoding: utf-8
"""
@author: lin
@file: 八皇后.py
@time: 2018/11/17 20:21
@desc:
"""
import copy
import numpy as np
def place(thisR,X):
    thisX = copy.deepcopy(X)
    for beforeR in range(thisR)[1:]:
        if (abs(thisR-beforeR)==abs(thisX[thisR]-thisX[beforeR]) or X[thisR]==X[beforeR]):
            return False
    return True
def main():
    wayList = [] # 方法集
    waySum = 0 # 表示总共的方法数
    n = int(input("请输入皇后个数："))
    X = [0]*(n+1)
    X[1]=0
    row=1
    while(row>0):
        X[row]+=1 # 第0列不使用，往右移动一列
        while (X[row]<=n) and  not(place(row,X)):X[row] +=1
        if(X[row]<=n): # 结点属于这一行内
            if row==n:
                waySum +=1
                wayList.append(copy.deepcopy(X[1:]))
            else:
                row +=1
                X[row]=0
        else:# 结点超出这一行范围
            row -=1
    wayList=np.array(wayList)-1
    if waySum==0:
        print("no way")
    else:
        print("waySum:",waySum)
        print("ways:",wayList)


if __name__=="__main__":
    while 1:
        main()