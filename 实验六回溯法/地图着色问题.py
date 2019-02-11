# encoding: utf-8
"""
@author: lin
@file: 地图着色问题.py
@time: 2018/11/21 18:16
@desc:
"""
import copy
import numpy as np
def dataLoad():
    map = []
    with open('mapData') as f:
        lines = f.readlines()
        for line in lines:
            lineData = []
            str = line.strip('\n').split(' ')
            for s in str:
                lineData.append(int(s))
            map.append(lineData)
    return map
# 检查着色要求
def Ok(row,X,map):
    thisX = copy.deepcopy(X)
    for i in range(len(thisX))[1:]:
        if(map[row-1][i-1]==1 and X[row]==X[i]):return False
    return True
def mColor():
    map = dataLoad()
    wayList = [] # 方法集
    waySum = 0 # 表示总共的方法数
    n = len(map)
    m = int(input("请输入着色个数："))
    X = [0]*(n+1)
    X[1]=0
    row=1
    while(row>0):
        X[row]+=1 # 第0列不使用，往右移动一列
        while (X[row]<=m) and  not(Ok(row,X,map)):X[row] +=1
        if(X[row]<=m): # 结点属于这一行内
            if row==n:
                waySum +=1
                wayList.append(copy.deepcopy(X[1:]))
            else:
                row +=1
                X[row]=0
        else:# 结点超出这一行范围
            row -=1
    wayList=np.array(wayList)
    if waySum==0:
        print("no way")
    else:
        print("waySum:",waySum)
        print("ways:",wayList)
        # 修改显示方法
        newWays= []
        for way in wayList:
            l = np.array(way)
            thisWay = []
            for i in range(m+1)[1:]:
                thisWay.append(list(np.where(l == i)[0]))
            newWays.append(thisWay)
        print(newWays)
        if [[0,4],[1],[2],[3]] in newWays:
            print(True)
        else:
            print(False)
if __name__=="__main__":
    while 1:
        mColor()

