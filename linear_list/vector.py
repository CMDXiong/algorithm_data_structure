# -*- coding:utf-8 -*-
__author__ = 'px'

from random import randint, seed


class Vector:
    def __init__(self, n):
        self.size = n  # 顺序表的大小
        self.count = 0  # 当前顺序表中存储元素数量
        self.arr = [None] * self.size  # 顺序表的底层存储结构

    def insert(self, pos, val):
        if pos < 0 or pos > self.count:
            return False
        if self.size == self.count and (not self.expand()):
            return False
        self.arr[pos+1:] = self.arr[pos:-1]
        self.arr[pos] = val

        self.count += 1

        return True

    def update(self, pos, val):
        if pos < 0 or pos > self.size:
            return False
        self.arr[pos] = val
        self.count += 1
        return True

    def delete(self, pos):
        if pos < 0 or pos >= self.count:
            return False

        self.arr[pos:-1] = self.arr[pos+1:]

        self.count -= 1

        return True

    def expand(self):
        """ 顺序表进行扩容"""
        if not self.arr:
            return False
        print("expand v from {} to {}".format(self.size, self.size*2))
        self.arr += [None] * self.size
        self.size *= 2

        return True

    def vector_seek(self, pos):
        if pos < 0 or pos > self.size:
            return False
        return self.arr[pos]

    def print(self):
        print(self.arr[0:self.count])
        print('\n')


if __name__ == "__main__":
    MAX_OP = 20

    vector = Vector(2)

    for i in range(MAX_OP):
        op = randint(1, 1000) % 5
        if op == 4:
            pos = randint(1, 1000) % (vector.count+2)
            print("delete item at {} from vector".format(pos))
            vector.delete(pos)
        else:
            num = randint(1, 1000)
            pos = randint(1, 1000) % (vector.count + 2)
            print("insert {} at {} to vector".format(num, pos))
            vector.insert(pos, num)
        vector.print()



