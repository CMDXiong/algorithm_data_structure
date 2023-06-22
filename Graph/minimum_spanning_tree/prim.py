# -*- coding:utf-8 -*-
__author__ = 'px'

import heapq

def minCostConnectPoints(points):
    def distance(x1, x2):
        dis = abs(x1[0]-x2[0]) + abs(x1[1]-x2[1])
        return dis

    nums_points = len(points)

    visited = [False] * nums_points

    edges = []

    for i in range(1, nums_points):
        dis = distance(points[0], points[i])
        heapq.heappush(edges, (dis, 0, i))

    visited[0] = True

    res = 0
    N = nums_points
    while edges and N > 0:
        dis, node1, node2 = heapq.heappop(edges)
        if not visited[node2]:
            visited[node2] = True
            res += dis
            for i in range(nums_points):
                if visited[i]:
                    continue
                dis = distance(points[node2], points[i])
                heapq.heappush(edges, (dis, node2, i))
            N -= 1

    return res

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

res = minCostConnectPoints(points)
print(res)
