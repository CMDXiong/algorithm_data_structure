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
    def __init__(self):
        self.heap = [-1] * 10
        self.len = 0

    def pop(self):
        """
        1. 首尾互换
        2. 从首位置元素，与左，右子孩子比较，与小者互换直到不能互换为止
        :return:
        """
        res = self.heap[0]
        self.swap(0, self.len-1)
        self.len -= 1
        self.shift_down(0)
        return res

    def add(self, num):
        self.heap[self.len] = num
        self.shift_up(self.len)
        self.len += 1

    def parent(self, i):
        return (i-1) // 2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def shift_down(self, i):

        while i < self.len:
            left = self.left(i)
            right = self.right(i)
            if left >= self.len:
                break
            elif right >= self.len:
                if self.heap[i] > self.heap[left]:
                    self.swap(i, left)
                    i = left
            else:
                if self.heap[left] > self.heap[right]:
                    j = right
                else:
                    j = left

                if self.heap[i] > self.heap[j]:
                    self.swap(i, j)
                    i = j
                else:
                    break

    def shift_up(self, i):
        if i > 0:
            parent = self.parent(i)
            if self.heap[parent] > self.heap[i]:
                self.swap(parent, i)
                self.shift_up(parent)


if __name__ == "__main__":
    min_heap = Heap()
    arr = [1, 6, 8, 3, 7, 9]
    for num in arr:
        min_heap.add(num)
    print(min_heap.heap)
    min_heap.pop()
    print(min_heap.heap)