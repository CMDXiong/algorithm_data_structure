# -*- coding:utf-8 -*-
__author__ = 'px'
""" 循环队列 """


from random import randint, seed
from linear_list.vector import Vector


class MyQueue:
    def __init__(self, n=10):
        self.data = Vector(n)
        self.size = n
        self.head = 0    # 队首元素位置
        self.tail = 0    # 队尾元素位置
        self.count = 0  # 队列中元素的个数

    def push(self, val):
        if self.full():
            return False
        self.data.update(self.tail, val)
        self.tail += 1
        if self.tail == self.size:
            self.tail = 0
        self.count += 1
        return True

    def pop(self):
        if self.empty():
            return False

        val = self.front()
        self.head += 1
        if self.head == self.size:
            self.head = 0
        self.count -= 1

        return val

    def front(self):
        """ 查看队首元素 """
        return self.data.vector_seek(self.head)

    def empty(self):
        return self.count == 0

    def full(self):
        return self.count == self.size

    def pprint(self):
        self.data.print()


if __name__ == "__main__":
    MAX_OP = 10

    queue = MyQueue(5)

    for i in range(MAX_OP):
        op = randint(1, 1000) % 5
        if op == 4 or op == 3:
            print("front of queue: ".format(queue.front()))
            queue.pop()

        else:
            num = randint(1, 1000)
            print("push {} to queue".format(num))
            queue.push(num)

    queue.pprint()


