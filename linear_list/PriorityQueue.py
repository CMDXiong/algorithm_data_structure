# -*- coding:utf-8 -*-
__author__ = 'px'
"""
优先队列实现
"""

from random import seed, randint


class PriorityQueue:
    def __init__(self, n=100):
        self.data = [None] * n
        self.n = 0  # 存储的元素个数
        self.size = n   # 队列大小

    def push(self, val):
        if self.full():
            return False

        self.data[self.n] = val
        self.n += 1
        self.shift_up(self.n-1)

        return True

    def pop(self):
        """ 弹出 """
        if self.empty():
            return False
        self.swap(0, self.n-1)
        self.n -= 1

        self.shift_down(0)

        return True

    def top(self):
        """ 查看队首元素"""
        if self.empty():
            return None
        return self.data[0]

    def empty(self):
        return self.n == 0

    def full(self):
        return self.n == self.size

    def parent(self, i):
        return (i-1) // 2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def shift_down(self, i):
        """
        向下调整
        1. 节点与左右子树节点值小的比较，更大则交换，直到不能交换
        """
        while self.left(i) < self.n:  # 有节点
            l = self.left(i)
            r = self.right(i)
            index = i   # 节点及子节点三者最大的索引
            if self.data[l] < self.data[index]:
                index = l
            if r < self.n and self.data[r] < self.data[index]:
                index = r

            if index == i:
                break

            self.swap(i, index)
            i = index

    def shift_up(self, i):
        """ 向上调整
        1. 与节点的父节点比较，小则交换，直到不能交换
        """
        # 1. 递归写法
        if i > 0:
            p = self.parent(i)
            if self.data[p] > self.data[i]:
                self.swap(p, i)
                self.shift_up(p)

        # # 2. 迭代写法
        # while i > 0:
        #     p = self.parent(i)
        #     if self.data[p] > self.data[i]:
        #         self.swap(p, i)
        #         i = p

    def pprint(self):
        print(self.data[0:self.n])
        print('\n')


if __name__ == "__main__":
    MAX_OP = 10
    seed(666)

    pri_queue = PriorityQueue(5)

    for i in range(MAX_OP):
        op = randint(1, 1000) % 5
        if op == 4 or op == 3:
            print("top of priority queue: {}".format(pri_queue.top()))
            pri_queue.pop()

        else:
            num = randint(1, 1000)
            print("push {} to priority queue".format(num))
            pri_queue.push(num)

        pri_queue.pprint()