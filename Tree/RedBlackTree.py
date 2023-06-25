# -*- coding:utf-8 -*-
__author__ = 'px'
"""
红黑树的python实现
"""

from enum import IntEnum
from random import sample, seed
from Tree.BaseTree import BaseTree, Node


class Color(IntEnum):
    RED = 0
    BLACK = 1
    DBLACK = 2


class RBNode(Node):
    def __init__(self, key, color=Color.RED, left=None, right=None):
        super(RBNode, self).__init__(key, left, right)
        self.color = color


NIL = RBNode(-1, Color.BLACK)  # 哨兵
NIL.left = NIL
NIL.right = NIL


class RedBlackTree(BaseTree):

    def __init__(self):
        super(RedBlackTree, self).__init__()
        self.root = NIL

    def insert(self, key):
        self.root = self._insert(self.root, key)
        self.root.color = Color.BLACK

    def _insert(self, root, key):
        if root is NIL:
            return RBNode(key, Color.RED, NIL, NIL)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        root = self.insert_maintain(root)
        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)
        self.root.color = Color.BLACK

    def _delete(self, root, key):
        if root is NIL:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # 删除度为0或1的结果，包括删除度为0的红色节点，度为0的黑色节点，度为1的黑色节点
            # 不存在度为1的红色节点
            if root.left == NIL or root.right == NIL:
                tmp = root.right if root.left == NIL else root.left
                tmp.color = int(root.color) + 1
                return tmp
            else:  # 删除度为2的节点, 转化成度为1的节点，进行删除
                pre_node = self.predecessor(root, NIL)
                root.key = pre_node.key
                root.left = self._delete(root.left, pre_node.key)


        root = self.delete_maintain(root)

        return root

    def insert_maintain(self, root):
        """
        进行插入失衡调整
        对root向下看两层：判断是否有失衡，下两层中有连续的红色节点，表示有失衡
        调整原则：调整前的路径和调整后的路径包含的黑节点个数不能变（相同）
        1. 插入: 主要是双红节点引起的失衡（参数root看成是grandfather）
            发生冲突的两个双红节点，上面为父节点(parent)，下面为子节点(x)，父节点的兄弟是uncle
            1. 如果uncle是红色:
                调整方案: uncle和父节点变成黑色，祖父变成红色
            2. 如果uncle是黑色
                1. LL型: 父节点出现在左子树，x出现在parent的左子树
                    调整方案:
                        1. 以grandfather为根进行右旋
                        2. 右旋后的新的根结点及其左右两个子节点颜色可以调整为红黑黑或者黑红红
                2. LR型: 以parent进行小左旋，再以grandfather进行右旋，最后进行红色上浮或者下层
                3. RR型: 与LL型相反调整
                4. RL型: 与LR相反调整

        2.
        """
        flag = 0  # 无冲突标记
        if root.left.color == Color.RED \
                and self.has_red_node(root.left):
            flag = 1  # 冲突在左子树
        if root.right.color == Color.RED \
                and self.has_red_node(root.right):
            flag = 2  # 冲突在右子树

        if flag == 0:  # 无冲突标记
            return root

        # 情况1: uncle是红色
        if root.left.color == Color.RED and \
                root.right.color == Color.RED:
            self.red_up_maintain(root)
            return root

        # 情况2: uncle是黑色
        if flag == 1:  # 冲突在左子树
            if root.left.right.color == Color.RED:  # LR型
                root.left = self.left_rotation(root.left)
            root = self.right_rotation(root)  # LL, LR

        if flag == 2:  # 冲突在右子树
            if root.right.left.color == Color.RED:  # RL型
                root.right = self.right_rotation(root.right)
            root = self.left_rotation(root)  # RR, RL

        # self.red_up_maintain(root)
        self.red_down_maintain(root)

        return root

    def red_up_maintain(self, root):
        root.color = Color.RED
        root.left.color = Color.BLACK
        root.right.color = Color.BLACK

    def red_down_maintain(self, root):
        root.color = Color.BLACK
        root.left.color = Color.RED
        root.right.color = Color.RED

    def has_red_node(self, root):
        """ 判断root是否有红色节点"""
        if root.left.color == Color.RED:
            return True
        if root.right.color == Color.RED:
            return True

        return False

    def delete_maintain(self, root):
        """ 删除调整
        主要是双重黑色引起的失衡（root看成父亲，看看子节点是否有失衡）
        """
        # 未失衡
        if root.left.color != Color.DBLACK and \
                root.right.color != Color.DBLACK:
            return root

        # 有双重黑节点
        # 1. 兄弟节点是红色，转化成兄弟节点的黑色的情况进行处理，
        # 同时需要进行颜色调整: 原根节点变成RED, 新根结点变成BLACK
        if self.has_red_node(root):
            root.color = Color.RED
            if root.left.color == Color.RED:
                root = self.right_rotation(root)
                root.right = self.delete_maintain(root.right)
            else:
                root = self.left_rotation(root)
                root.left = self.delete_maintain(root.left)
            root.color = Color.BLACK
            return root

        # 2. 兄弟节点是黑色：按兄弟节点的子孩子有没有红色节点分三种情况
        # 2.1 兄弟节点的没有红色子孩子, 调整根结点颜色+1, 两侧子节点颜色-1
        if (root.left.color == Color.DBLACK and (not self.has_red_node(root.right))) \
                or (root.right.color == Color.DBLACK and (not self.has_red_node(root.left))):
            root.color += 1
            root.left.color -= 1
            root.right.color -= 1
            return root

        # 2.2 兄弟节点的有红色子孩子
        # 颜色调整方案:
        # 新根节点颜色调整为原根节点的颜色, 两个子节点颜色调整为黑

        # 双重黑在右子树
        old_root_color = root.color
        if root.right.color == Color.DBLACK:
            if root.left.left.color != Color.RED:  # LR型
                root.left = self.left_rotation(root.left)
            root = self.right_rotation(root)

        else:  # 双重黑在左子树
            if root.right.right.color != Color.RED:  # RL型
                root.right = self.right_rotation(root.right)
            root = self.left_rotation(root)

        root.color = old_root_color  # 新根节点颜色调整为原根节点的颜色
        root.left.color = root.right.color = Color.BLACK
        return root


def output(root):
    if root is NIL:
        return
    print_str = "{}| {}".format(root.color, root.key)
    if root.left:
        print_str += " " + str(root.left.key)
    if root.right:
        print_str += " " + str(root.right.key)
    print_str += '\n'

    print(print_str)
    output(root.left)
    output(root.right)


if __name__ == "__main__":
    seed(10)
    MAX_N = 10
    rb_tree = RedBlackTree()
    nums = sample(range(1, 50), MAX_N)
    print(nums)
    for num in nums:
        print("insert {} to red black tree: ".format(num))
        rb_tree.insert(num)
        output(rb_tree.root)

    while True:
        x = input("输入一个数: ")
        if x == 'q':
            break
        x = int(x)
        print("delete {} from red black tree: ".format(x))
        rb_tree.delete(x)
        output(rb_tree.root)

