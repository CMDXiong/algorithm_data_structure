# -*- coding:utf-8 -*-
__author__ = 'px'

"""
python 实现BST(二叉查找树)
"""

from Tree.BaseTree import BaseTree, Node


class BST(BaseTree):
    def __init__(self):
        super(BST, self).__init__()

    def get(self, key):
        return self._get(self.root, key)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None and root.right is None:  # 度为0的节点
                return None
            elif root.left is None or root.right is None:  # 度为1的节点
                tmp = root.left if root.left else root.right
                return tmp
            else:  # 度为2的节点
                tmp = self.predecessor(root)  # 前驱结点
                root.key = tmp.key
                root.left = self._delete(root.left, tmp.key)

        return root

    def _get(self, node, key):
        # 获取键为key的节点
        while node:
            if node.value > key:
                node = node.left
            elif node.value == key:
                return node
            elif node.value < key:
                node = node.right
        return None


if __name__ == "__main__":
    keys = [10, 3, 15, 8, 5, 9, 11]
    bst = BST()
    root = None
    for key in keys:
        bst.insert(key)
    bst.in_order()

    for key in keys:
        bst.delete(key)
        print(key, ": 删除")
        bst.in_order()


