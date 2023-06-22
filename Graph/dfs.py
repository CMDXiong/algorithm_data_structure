# -*- coding:utf-8 -*-
__author__ = 'px'

# 每一个点有有三种状态：1：表示未访问，2：访问但是未处理，3：已经处理


def dfs(graph):
    def dfs_visit(i):
        for j in range(n):
            if graph[i][j] == 1 and status[j] == 1:
                status[j] = 2
                dfs_visit(j)

        status[i] = 3
        print(i)

    n = len(graph)
    status = [1] * n

    for i in range(n):
        if status[i] == 1:
            status[i] = 2
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

