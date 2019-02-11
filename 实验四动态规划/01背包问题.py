# encoding: utf-8
"""
@author: lin
@file: 01KnapsackProblem.py
@time: 2018/10/19 18:29
@desc:参考CSDN网页：https://blog.csdn.net/mu399/article/details/7722810?tdsourcetag=s_pctim_aiomsg
"""
import numpy as np
class PackageItem:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
def get01PackageAnswer(bagItems, bagSize):
    bagMatrix = np.zeros((len(bagItems), bagSize+1))
    for i in range(bagSize+1)[1:]:
        for j in range(len(bagItems)):
            item = bagItems[j]
            # 这个物品重量大于背包乘重
            if item.weight > i:
                if j == 0:
                    bagMatrix[j][i] = 0
                else:
                    bagMatrix[j][i] = bagMatrix[j-1][i]
            # 这个物品重量小于背包乘重
            else:
                # 只有一个物品
                if j == 0:
                    bagMatrix[j][i] = item.value
                    continue
                else:
                    itemInBag = bagMatrix[j-1][i-item.weight] + item.value
                bagMatrix[j][i] = bagMatrix[j-1][i] if bagMatrix[j-1][i] > itemInBag else itemInBag

    print(bagMatrix)
    # find answer
    answer = []
    curSize = bagSize
    for i in range(len(bagItems))[::-1]:
        item = bagItems[i]
        if curSize == 0:
            break
        if i == 0 and curSize > 0:
            answer.append(item.name)
            break
        if bagMatrix[i][curSize]-bagMatrix[i-1][curSize-item.weight] == item.value:
            answer.append(item.name)
            curSize -= item.weight
    return answer
def main():
    nameArr = ['a', 'b', 'c', 'd', 'e']
    weightArr = [2, 2, 6, 5, 4]
    valueArr = [6, 3, 5, 4, 6]
    bagItems = []
    for i in range(len(nameArr)):
        bagItems.append(PackageItem(nameArr[i], weightArr[i], valueArr[i]))
    ans = get01PackageAnswer(bagItems, 10)
    sumWeight = 0
    sumValue = 0
    for a in ans:
        for item in bagItems:
            if item.name==a:
                sumWeight += item.weight
                sumValue += item.value
    print(ans)
    print('sumWeight:', sumWeight, ' sumValue:', sumValue )
if __name__=="__main__":
    main()