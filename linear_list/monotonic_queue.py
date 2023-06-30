# -*- coding:utf-8 -*-
__author__ = 'px'

""" 单调队列"""

from collections import deque


if __name__ == "__main__":
    k = 3  # 区间长度
    q = deque()  # 模拟单调递增队列

    arr = [3, 1, 4, 5, 2, 9, 8, 12]
    print("ind: ", list(range(len(arr))))
    print("arr: ", arr)

    for i, val in enumerate(arr):
        # 1. 入队
        while q and (arr[q[-1]] > val):
            q.pop()
        q.append(i)

        # 2. 出队
        if i - q[0] == k:
            q.popleft()

        print("[{}, {}] = arr[{}] = {}".format(max(i-k+1, 0), i, q[0], arr[q[0]]))

