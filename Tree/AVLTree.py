# -*- coding:utf-8 -*-
__author__ = 'px'

"""
python 实现AVL
"""
from Tree.BaseTree import BaseTree, Node


class AVLNode(Node):
    def __init__(self, key, h=1):
        super(AVLNode, self).__init__(key)
        self.h = h  # 树高


class AVLTree(BaseTree):
    def __init__(self):
        super(AVLTree, self).__init__()

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, root, key):
        if root is None:
            return None

        if key < root.key:
            return self._find(root.left, key)
        elif key > root.key:
            return self._find(root.right, key)
        else:
            return root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return AVLNode(key, 1)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        self.updata_height(root)
        root = self.maintain(root)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # 度为0或1的情况
            if root.left is None or root.right is None:
                tmp = None
                if root.left:
                    tmp = root.left
                if root.right:
                    tmp = root.right
                return tmp
            else:  # 度为2的情况
                pre_node = self.predecessor(root)
                root.key = pre_node.key
                root.left = self._delete(root.left, pre_node.key)
                return root

        self.updata_height(root)
        root = self.maintain(root)
        return root


    def left_rotation(self, old_root):
        """ 左旋"""
        print("left rorate: ", old_root.key)
        new_root = old_root.right
        old_root.right = new_root.left
        new_root.left = old_root

        self.updata_height(old_root)
        self.updata_height(new_root)

        return new_root

    def right_rotation(self, old_root):
        """ 右旋"""
        print("right rorate: ", old_root.key)
        new_root = old_root.left
        old_root.left = new_root.right
        new_root.right = old_root

        self.updata_height(old_root)
        self.updata_height(new_root)

        return new_root

    def updata_height(self, node):
        h = 0
        if node.left:
            h = max(h, node.left.h)
        if node.right:
            h = max(h, node.right.h)

        node.h = h+1

    def maintain(self, root):
        if root is None:
            return root

        h_l, h_r = self._h_child(root)
        if abs(h_l-h_r) < 2:
            return root

        if h_l > h_r:  # 左子树高于右子树
            h_r_l, h_r_r = self._h_child(root.left)
            if h_r_l < h_r_r:  # LR型
                root.left = self.left_rotation(root.left)
            root = self.right_rotation(root)  # LL型和LR型都需要大右旋转
        else:
            h_l_l, h_l_r = self._h_child(root.right)
            if h_l_l > h_l_r:  # RL型
                root.right = self.right_rotation(root.right)
            root = self.left_rotation(root)  # RL型和RR型都需要大左旋转

        return root

    def _h_child(self, root):
        """ 子树的高度 """
        h_left, h_right = 0, 0
        if root.left:
            h_left = root.left.h
        if root.right:
            h_right = root.right.h

        return h_left, h_right


if __name__ == "__main__":
    arr = [5, 9, 8, 3, 2, 4, 1, 7]
    # arr = [5, 9, 8]
    avl_tree = AVLTree()
    for key in arr:
        avl_tree.insert(key)

    node = avl_tree.find(8)
    print("height: ", node.h)  # 2

    for key in arr:
        print("delete: ", key)
        avl_tree.delete(key)
        avl_tree.in_order()


