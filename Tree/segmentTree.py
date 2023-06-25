
# -*- coding:utf-8 -*-
__author__ = 'px'
"""
线段树

参考：
1. https://blog.csdn.net/qq_41750911/article/details/125097537
2. https://huterox.blog.csdn.net/article/details/129230594?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-129230594-blog-125097537.235%5Ev38%5Epc_relevant_anti_vip_base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-129230594-blog-125097537.235%5Ev38%5Epc_relevant_anti_vip_base&utm_relevant_index=2
"""

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr  # 原数据
        self.len = len(self.arr)
        self.tree = [0] * 4 * self.len  # 线段树

    def build_segment_tree(self, node, start, end):
        """
        根据具体的区间范围，建立线段树
        :param node:
        :param start:
        :param end:
        :return:
        """
        if start == end:   # 叶子结点
            self.tree[node] = self.arr[start]
            return

        mid = (start+end)//2

        left = self.left(node)
        right = self.right(node)

        self.build_segment_tree(left, start, mid)
        self.build_segment_tree(right, mid+1, end)

        self.tree[node] = self.tree[left] + self.tree[right]

    def update_tree(self, node, start, end, index, value):
        """
        更新树，单点修改
        1. 如果要查询的区间完全覆盖当前区间，就直接返回当前区间的值；
        2. 如果查询区间和左孩子有交集，则搜索左孩子；
        3. 如果查询区间和右孩子有交集，就搜索右孩子；
        4. 最后合并处理两边查询的数据。

        :param node: 当前结点位置
        :param start:
        :param end:
        :param index: 待更新的结点位置
        :param value: 待更新的值
        :return:
        """
        if start == end:
            self.tree[node] = value
            return

        mid = (start+end)//2
        left_node = self.left(node)
        right_node = self.right(node)
        if start <= index <= mid:    # 左区间
            self.update_tree(left_node, start, mid, index, value)
        else:   # 右区间
            self.update_tree(right_node, mid+1, end, index, value)

        # 更新结点值
        self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def query_tree(self):
        pass

    def print_segment_tree(self):
        root = Node(0)
        self.build_segment_tree(root, 0, 4)
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            print(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def parent(self, i):
        return (i-1)//2


if __name__ == "__main__":
    segment_tree = SegmentTree([0,1,2,3,4])
    segment_tree.print_segment_tree()
