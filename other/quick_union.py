# -*- coding:utf-8 -*-
__author__ = 'px'

from random import randint


class QuickUnion:
    def __init__(self, n):
        """
        :param n: n个节点
        """
        self.parent = [-1] * n

    def find(self, x):
        while self.parent[x] != -1:
            x = self.parent[x]
        return x

        # 递归
        # if self.parent[x] == -1:
        #     return x
        # return self.find(self.parent[x])

    def union(self, x, y):
        """ 规定将x挂在y上"""
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False

        self.parent[x_root] = y_root
        return True

    def print(self):
        n = len(self.parent)
        subs1 = " ".join([str(i).zfill(2) for i in range(n)])
        print(subs1)

        print("-" * (3*n-1))

        sub_color = " ".join([str(color).zfill(2) for color in self.parent])
        print(sub_color)


if __name__ == "__main__":
    MAX_OP = 15
    colors = [randint(1, 50) for _ in range(MAX_OP)]
    quick_union = QuickUnion(MAX_OP)
    quick_union.print()
    nodes = input("union: ")
    while nodes != 'q':
        nums = [int(x) for x in nodes.split()]
        quick_union.union(*nums)
        quick_union.print()

        nodes = input("merge: ")