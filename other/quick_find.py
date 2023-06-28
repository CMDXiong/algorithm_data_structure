# -*- coding:utf-8 -*-
__author__ = 'px'
from random import randint, seed


class UnionQuick:
    def __init__(self, colors):
        """
        :param color: list, 下标代表第i个点, 值代表节点颜色
        """
        self.colors = colors  # list

    def find(self, node):
        """ 返回node的颜色"""
        return self.colors[node]

    def merge(self, node1, node2):
        """ uqf 所有color1颜色节点变成color2"""
        color1 = self.colors[node1]
        color2 = self.colors[node2]

        if color1 == color2:
            return False

        for i in range(len(self.colors)):
            if self.find(i) == color1:
                self.colors[i] = color2

        return True

    def print(self):
        n = len(self.colors)
        subs1 = " ".join([str(i).zfill(2) for i in range(n)])
        print(subs1)

        print("-" * (3*n-1))

        sub_color = " ".join([str(color).zfill(2) for color in self.colors])
        print(sub_color)


if __name__ == "__main__":
    MAX_OP = 30
    colors = [randint(1, 50) for _ in range(MAX_OP)]
    union_quick = UnionQuick(colors)
    union_quick.print()
    nodes = input("merge: ")
    while nodes != 'q':
        nums = [int(x) for x in nodes.split()]
        union_quick.merge(*nums)
        union_quick.print()

        nodes = input("merge: ")