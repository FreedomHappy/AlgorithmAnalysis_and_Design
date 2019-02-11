# encoding: utf-8
"""
@author: lin
@file: ShortestPaths.py
@time: 2018/12/5 22:04
@desc:
"""
import math
import heapq
class MinHeapNode:
    def __init__(self):
        self.i=None #顶点编号
        self.length=None #当前路长
    def getLength(self):
        return self.length

    def __lt__(self, other):  # operator <
        return self.length < other.length

def ShortestPaths(v,graph):
    H = [] # 优先级列表
    n = len(graph) #城市数
    E = MinHeapNode()
    E.i=v
    E.length=0
    dist = [math.inf]*n
    prev = [0]*n
    dist[v]=0
    #搜索问题的解空间
    while(1):
        for j in range(n):
            if((graph[E.i][j]<math.inf) and (E.length+graph[E.i][j]<dist[j])):
                #顶点i到顶点j可达，且满足控制约束
                dist[j]=E.length+graph[E.i][j]
                prev[j]=E.i
                #加入活结点优先队列
                N = MinHeapNode()
                N.i=j
                N.length=dist[j]
                heapq.heappush(H,N)
        if len(H)==0:
            break
        else:
            E = heapq.heappop(H)
    print(dist)
    print(prev)
    for this in range(len(prev)):
        printPath(v,this,prev)
        print(':',dist[this])
def printPath(v,this,prev):
    if this==v:
        print(this+1,end="")
    else:
        length = printPath(v,prev[this],prev)
        print("--", this+1, end="")
def main():
    graph=[[0,10,math.inf,30,100],
           [math.inf,0,50,math.inf,math.inf],
           [math.inf,math.inf,0,math.inf,10],
           [math.inf,math.inf,20,0,60],
           [math.inf,math.inf,math.inf,math.inf,0]]
    ShortestPaths(0,graph)
    pass
if __name__=="__main__":
    main()