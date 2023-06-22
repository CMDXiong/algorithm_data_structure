# -*- coding:utf-8 -*-
__author__ = 'px'

"""
python 实现BST(二叉查找树)
"""


class Node:
    def __init__(self, key, value, N, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.N = N  # 以该结点为根的子树中的结点总数


class BST:
    def __init__(self):
        self.root = None
        pass

    def get(self, key):
        # 获取键为key的值
        return self.get_node(self.root)

    def get_node(self, node, key):
        # 获取以node为根结点，键为key的值
        cur_node = node
        while cur_node:
            if cur_node.value > key:
                cur_node = cur_node.left
            elif cur_node.value == key:
                return cur_node.value
            elif cur_node.value < key:
                cur_node = cur_node.right

        return None

    def put(self, key, value):
        # 时间复杂度：最好O(lgN), 最差O(N)
        self.root = self.put_node(self.root, key, value)

    def put_node(self, node, key, value):
        # 将(key, value)插入到以node为根结点的BST中
        if node is Node:
            return Node(key, value, 1)

        cur = node
        add_node = Node(key, value, 1)
        while cur:
            if cur.value > key:
                cur.N += 1
                cur = cur.left
                if cur.left is None:
                    cur.left = add_node
                    break
            elif cur.value == key:
                cur.value = value
                break
            elif cur.value < key:
                cur.N += 1
                cur = cur.right
                if cur.right is None:
                    cur.right = add_node
                    break
        return node

    def size(self):
        return self.size_node(self.root)

    def size_node(self, node):
        if node is not None:
            return node.N
        return 0

    def max(self):
        cur = self.root
        while cur:
            if cur.right is Node:
                return cur.value
            else:
                cur = cur.right

    def min(self):
        cur = self.root
        while cur:
            if cur.left is Node:
                return cur.value
            else:
                cur = cur.left

    def delete(self, key):
        pass

    def delete_min(self, key):
        pass

    def delete_max(self, key):
        pass

    def keys(self):
        pass

