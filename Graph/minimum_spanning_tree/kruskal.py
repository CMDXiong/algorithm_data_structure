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
            return True
        return False


def minCostConnectPoints(points):
    def distance(x1, x2):
        dis = abs(x1[0]-x2[0]) + abs(x1[1]-x2[1])
        return dis

    nums_points = len(points)

    union_find = UnionFind(nums_points)

    edges = []
    for i in range(nums_points):
        for j in range(i+1, nums_points):
            edges.append((distance(points[i], points[j]), i, j))

    edges.sort()

    res = 0
    edge_nums = 0
    for dis, x, y in edges:
        if union_find.union(x, y):
            res += dis
            edge_nums += 1
        if edge_nums == nums_points - 1:
            break

    return res

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

res = minCostConnectPoints(points)
print(res)