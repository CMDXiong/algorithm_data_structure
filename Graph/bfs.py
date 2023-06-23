# -*- coding:utf-8 -*-
__author__ = 'px'

"""
bfs: 
1. bfs遍历邻接矩阵
2. bfs遍历邻接链表

无权图的最短路径可以使用bfs
"""

from collections import deque
from enum import Enum


class Color(Enum):
    WHITE = 1   # 代表未访问
    GRAY = 2    # 代表第一次被发现
    BLACK = 3   # 代表已处理完成


class Node:
    def __init__(self, key):
        self.d = 0  # 距离源结点的距离
        self.p = None  # 结点的前驱结点
        self.color = Color.WHITE   # 结点的颜色，代表一种状态
        self.key = key  # 结点的标号


def bfs(graph, key: int):
    """
    :param graph: 邻接矩阵表示的图
    :param key: 结点标号
    :return:
    """
    n = len(graph)  # 图中结点个数
    nodes = [Node(i) for i in range(n)]
    # visited = [False] * n
    # visited[v] = True
    nodes[key].color = Color.GRAY
    q = deque()
    q.append(nodes[key])

    while q:
        i_node = q.popleft()
        i_node_key = i_node.key
        print(i_node_key)  # 打印访问的结点号
        for j in range(n):
            node = nodes[j]
            if node.color == Color.WHITE and graph[i_node_key][j] == 1:
                node.color = Color.GRAY
                node.p = i_node
                node.d += 1
                q.append(node)

        i_node.color = Color.BLACK

    return nodes


# 打印s到v的最短路径
def print_shortest_path(nodes, s_key, v_key):
    v_node = nodes[v_key]
    if v_key == s_key:
        print(s_key)
    elif v_node.p is None:
        print("no path from {} to {} exists".format(s_key, v_key))
    else:
        print_shortest_path(nodes, s_key, v_node.p.key)
        print(v_key)


# 打印s到v的最短路径, 非递归写法
def print_shortest_path_no_rec(nodes, s_key, v_key):
    shortest_path = []
    v_node = nodes[v_key]
    while s_key != v_node.key:
        if v_node.p is None:
            print("no path from {} to {} exists".format(s_key, v_key))
            return []
        shortest_path.append(v_node.key)
        v_node = v_node.p

    shortest_path.append(s_key)

    shortest_path.reverse()
    print(shortest_path)
    return shortest_path


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 1, 0]
    ]

    nodes = bfs(graph, 0)

    print("rec: ")
    print_shortest_path(nodes, 0, 3)

    print("no rec: ")
    print_shortest_path_no_rec(nodes, 0, 6)
