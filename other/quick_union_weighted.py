# -*- coding:utf-8 -*-
__author__ = 'px'

from random import randint


class QuickUnionWeighted:

    def __init__(self, n):
        """
        :param n: n个节点
        """
        self.parent = [-1] * n
        self.size = [1] * n  # 值代表以第i个节点为根节点的树拥有的节点个数

    def find(self, x):
        x_copy = x
        while self.parent[x] != -1:
            x = self.parent[x]
        self.parent[x_copy] = x  # 路径压缩
        return x

        # 递归
        # if self.parent[x] == -1:
        #     return x
        # self.parent[x] = self.find(self.parent[x]) # 路径压缩
        # return self.parent[x]

    def union(self, x, y):
        """ 规定将x挂在y上"""
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False

        # 节点少的挂在节点多的树上
        if self.size[x_root] < self.size[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        else:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]

        return True

    def print(self):
        n = len(self.parent)
        subs1 = " ".join([str(i).zfill(2) for i in range(n)])
        print(subs1)

        print("-" * (3 * n - 1))

        sub_color = " ".join([str(color).zfill(2) for color in self.parent])
        print(sub_color)
        size_str = " ".join([str(size).zfill(2) for size in self.size])
        print(size_str)


if __name__ == "__main__":
    MAX_OP = 15
    colors = [randint(1, 50) for _ in range(MAX_OP)]
    quick_union = QuickUnionWeighted(MAX_OP)
    quick_union.print()
    nodes = input("union: ")
    while nodes != 'q':
        nums = [int(x) for x in nodes.split()]
        quick_union.union(*nums)
        quick_union.print()

        nodes = input("merge: ")