# -*- coding:utf-8 -*-
__author__ = 'px'
"""
时间复杂度：O(V+E)
空间复杂度：O(V)
"""


from enum import Enum


# 每一个点有有三种状态：1：表示未访问，2：访问但是未处理，3：已经处理
class Color(Enum):
    WHITE = 1   # 代表未访问
    GRAY = 2    # 代表第一次被发现
    BLACK = 3   # 代表已处理完成


class Node:
    def __init__(self, key):
        self.d = 0  # 第一次被发现的时间
        self.f = 0  # 结点搜索完成的时间
        self.p = None  # 结点的前驱结点
        self.color = Color.WHITE   # 结点的颜色，代表一种状态
        self.key = key  # 结点的标号


def dfs(graph):
    def dfs_visit(i):
        nonlocal time
        time += 1
        i_node = nodes[i]
        i_node.d = time
        for j in range(n):
            j_node = nodes[j]
            if graph[i][j] == 1 and j_node.color == Color.WHITE:
                j_node.color = Color.GRAY
                dfs_visit(j)

        i_node.color = Color.BLACK
        time += 1
        i_node.f = time
        print(i)

    n = len(graph)
    nodes = [Node(i) for i in range(n)]
    time = 0

    for i in range(n):
        node = nodes[i]
        if node.color == Color.WHITE:
            node.color = Color.GRAY
            dfs_visit(i)


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 1, 0],

    ]

    dfs(graph)

