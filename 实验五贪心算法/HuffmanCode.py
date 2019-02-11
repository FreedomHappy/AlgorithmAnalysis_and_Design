# encoding: utf-8
"""
@author: lin
@file: HuffmanCode.py
@time: 2018/10/29 21:09
@desc:
"""
# encoding: utf-8
"""
@author: lin
@file: 霍夫曼编码.py
@time: 2018/10/29 20:12
@desc:
"""
# 定义节点类
class Node:
    def __init__(self, name=None, weight=None):
        self.name = name
        self.weight = weight
        self.parent = None
        self.left = None
        self.right = None
        self.id = None


# 生成新节点
def generate_node(l, w):
    list = []
    for name, weight in zip(l, w):
        list.append(Node(name, weight))
    return list

# 按权值排序
def sort(list):
    return sorted(list, key=lambda Node: Node.weight)

# Huffman编码
def HuffmanTree(list):
    list = sort(list)
    while len(list)!=1:
        a, b = list[0], list[1]
        new = Node()
        new.weight = a.weight + b.weight
        new.left = a
        new.right = b
        a.parent = new
        b.parent = new
        list.remove(a)
        list.remove(b)
        list.append(new)
        list = sort(list)
    return list


# 前序遍历
def pre_order(root, code, codelist):
    if root is None:
        code = code[:-1]
        return
    pre_order(root.left, code+'0', codelist)
    if root.name is not None:
        print(root.name, ' 的权重为:', root.weight, ',编码为', code)
        if root.weight not in codelist:
            codelist[root.weight] = code
    pre_order(root.right, code+'1', codelist)

def main():
    l = ['a', 'b', 'c', 'd', 'e']
    w = [5, 4, 3, 2, 1]
    list = generate_node(l, w)
    list = HuffmanTree(list)
    code = ''
    codelist = {}
    pre_order(list[0], code, codelist)
    print(sorted(codelist.items(), reverse=True))

if __name__ == "__main__":
    main()

