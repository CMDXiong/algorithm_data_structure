# -*- coding:utf-8 -*-
__author__ = 'px'

"""
bfs: 
1. bfs遍历邻接矩阵
2. bfs遍历邻接链表

无权图的最短路径可以使用bfs
"""

from collections import deque


def bfs(graph, v: int):
    """
    :param graph: 邻接矩阵表示的图
    :param v: 结点标号
    :return:
    """
    n = len(graph)  # 图中结点个数
    visited = [False] * n
    visited[v] = True

    q = deque()
    q.append(v)

    while q:
        node_num = q.popleft()
        print(node_num)  # 打印访问的结点
        for j in range(n):
            if not visited[j] and graph[node_num][j] == 1:
                visited[j] = True
                q.append(j)


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

    bfs(graph, 0)
