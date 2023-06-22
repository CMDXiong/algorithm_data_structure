# -*- coding:utf-8 -*-
__author__ = 'px'


class UnionFind:
    def __init__(self, n):

        self.parent = [-1] * n

    def find(self, x):
        while self.parent[x] != -1:
            x = self.parent[x]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[x_root] = y_root


class UnionFindRank:
    def __init__(self, n):

        self.parent = [-1] * n
        self.rank = [0] * n

    def find(self, x):
        x_root = x
        while self.parent[x_root] != -1:
            x_root = self.parent[x_root]
        return x_root

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            elif self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            else:
                self.parent[x_root] = y_root
                self.rank[y_root] += 1


# 路径压缩
class UnionFindRankPro:
    def __init__(self, n):

        self.parent = [-1] * n
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == -1:
            return x
        else:
            # 路径压缩
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            elif self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            else:
                self.parent[x_root] = y_root
                self.rank[y_root] += 1



