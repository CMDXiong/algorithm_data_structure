# -*- coding:utf-8 -*-
__author__ = 'px'
"""
最小堆：最小堆是一棵完全二叉树，非叶子结点的值不大于左孩子和右孩子的值

一般都用数组来表示堆，i结点的父结点下标就为(i–1)/2。
它的左右子结点下标分别为2 * i + 1和2 * i + 2。
    10
 15     56
25 30 70

存储：[10, 15, 56, 25, 30, 70]
"""


class Heap:
    def __init__(self, data=None):
        if data is None:
            self.data = [-1] * 10
            self.n = 0
        else:
            self.data = data
            self.n = len(data)
            self.heapify(self.data)

    def pop(self):
        """
        1. 首尾互换
        2. 从首位置元素，与左，右子孩子比较，与小者互换直到不能互换为止
        :return:
        """
        res = self.data[0]
        self.swap(0, self.n - 1)
        self.n -= 1
        self.shift_down(0)
        return res

    def add(self, num):
        self.data[self.n] = num
        self.shift_up(self.n)
        self.n += 1

    def heapify(self, data):
        """ 将data数组线性堆化，即建立最小堆"""
        n = len(data)
        for i in range(n//2, 0, -1):
            self.shift_down(i)
        return data

    def heap_sort(self, data):
        """ 将data数组进行堆排序"""
        heap = Heap(data)
        n = heap.n
        for i in range(n-1, 0, -1):
            heap.swap(0, i)
            heap.shift_down(0, i)
        return heap.data

    def parent(self, i):
        return (i-1) // 2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def shift_down(self, i, n=None):
        """
        向下调整
        1. 节点与左右子树节点值小的比较，更大则交换，直到不能交换
        :param n: 数组前n位进行向下调整
        """
        if n is None:
            n = self.n

        while self.left(i) < n:  # 有节点
            l = self.left(i)
            r = self.right(i)
            index = i  # 节点及子节点三者最大的索引
            if self.data[l] < self.data[index]:
                index = l
            if r < n and self.data[r] < self.data[index]:
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


if __name__ == "__main__":
    min_heap = Heap()
    arr = [1, 6, 8, 3, 7, 9]
    res = min_heap.heap_sort(arr)
    print(res)
    # min_heap.heapify(arr)
    # print(arr)
    # for num in arr:
    #     min_heap.add(num)
    # print(min_heap.data)
    # min_heap.pop()
    # print(min_heap.data)