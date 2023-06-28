# -*- coding:utf-8 -*-
__author__ = 'px'
""" 链表 """
from random import randint, seed


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class List:
    def __init__(self, head=None):
        self.head = head

    def insert_head(self, pos, val):
        """ 有头思想 插入"""
        dummy = Node(next=self.head)

        # 找到插入位置的前一个元素
        p, node = dummy, Node(val)
        for _ in range(pos):
            p = p.next

        node.next = p.next
        p.next = node

        self.head = dummy.next
        return self.head

    def insert(self, pos, val):
        """无头思想"""
        node = Node(val)
        if pos == 0:
            node.next = self.head
            self.head = node
            return self.head

        # 找到插入位置的前一个元素
        p = self.head
        for _ in range(pos-1):
            p = p.next

        node.next = p.next
        p.next = node

        return self.head

    def delete(self):
        pass

    def find(self, val):
        p = self.head
        while p:
            if p.data == val:
                return True
        return False

    def find_interesting(self, val):
        p = self.head
        p_num = ""
        p_str = ""
        num = 0

        while p:
            p_num += str(num)
            p_str += str(p.data)
            if p.data == val:
                p_3 = " " * (len(p_str) - 2) + "|"
                p_4 = " " * (len(p_str) - 2) + "^"
                print(p_num)
                print(p_str)
                print(p_3)
                print(p_4)
                print('\n')
                return True
            if p.next:
                p_num += " ->  "
                p_str += " -> "

            p = p.next
            num += 1

        print(p_num)
        print(p_str)
        print('\n')
        return False

    def print(self):
        p = self.head
        p_num = ""
        p_str = ""
        num = 0
        while p:
            p_num += str(num)
            p_str += str(p.data)
            if p.next:
                p_num += " ->  "
                p_str += " -> "
            p = p.next
            num += 1
        print(p_num)
        print(p_str)
        print('\n')


if __name__ == "__main__":
    MAX_OP = 6
    seed(666)

    my_list = List()

    for i in range(MAX_OP):
        pos = randint(1, 1000) % (i+1)
        val = randint(1, 100)
        print("insert {} at {} to list".format(val, pos))
        my_list.insert_head(pos, val)

        print("find {} in list".format(val, pos))
        # my_list.find(val)
        my_list.print()
