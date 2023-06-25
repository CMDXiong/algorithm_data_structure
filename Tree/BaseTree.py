# -*- coding:utf-8 -*-
__author__ = 'px'

"""
python 实现BST(二叉查找树)
"""


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BaseTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, root, key):
        if root is None:
            return None

        while root:
            if root.key == key:
                return root
            elif root.key > key:
                root = root.left
            else:
                root = root.right

    def predecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node

    def successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node

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

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, root):
        if root is None:
            return
        self._in_order(root.left)
        print(root.key)
        self._in_order(root.right)



