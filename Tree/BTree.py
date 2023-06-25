# -*- coding:utf-8 -*-
__author__ = 'px'

"""
索引为何不用散列来做？
    1. 哈希函数设计索引，会存在哈希冲突，导致散列不均匀，存在大量的线性查找
    2. 在范围查找时，会退化成线性查找，hash不合适
    3. 优点是等值查询比较快 
"""


class BTreeNode:
    def __init__(self, n=0, leaf=False):
        """
        keys数组中i个key，左边孩子为child[i],右边孩子为child[i+1]
        :param n:
        :param leaf:
        """
        self.n = n          # 关键字的个数
        self.keys = []      # 包含的关键字
        self.child = []     # 结点的孩子
        self.leaf = leaf    # 是否为叶子结点


class BTree:
    def __init__(self, m, root=None):
        self.m = m  # 内部结点至少要有t个孩子
        # self.max_key = 2*self.t - 1  # 结点包含键的最大数量
        # self.max_child = self.max_key + 1  # 节点包含的最大孩子个数

        self.root = root

    def search(self, key, node=None):
        if node is None:
            return self.search(key, self.root)

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        # 找到
        if i < len(node.keys) and key == node.keys[i]:
            return node, i
        elif node.leaf:  # 叶子结点
            return None
        else:  # 从叶子结点中寻找
            return self.search(key, node.child[i])

    def insert(self, root, key):
        root = self._insert(root, key)
        if root.n == self.n:
            p = BTreeNode()
            p.child.append(root)
            root = self.insert_maintain(p, root, 0)

        return root

    def insert_key(self, node, key):
        """
        将key插入到node，此时并不考虑node是否满足B树结点条件
        :param node:
        :param key:
        :return:
        """
        if node is None:
            node = BTreeNode()
            node.keys.append(key)
            node.n += 1
            return node
        else:
            pos = 0
            while pos < node.n and node.keys[pos] < key:
                pos += 1
            if node.keys[pos] == key:
                return node
            else:
                node.keys.append(key)
                node.n += 1
                node[pos+1:node.n] = node[pos:node.n-1]
                node[pos] = key
                return node

    def _insert(self, node, key):
        # node为空或为终端结点
        if node is None or (not node.child):
            return self.insert_key(node, key)
        pos = 0
        while pos < node.n and key > node.keys[pos]:
            pos += 1
        if pos < node.n and key == node.keys[pos]:
            return node

        self._insert(node.child[pos], key)
        return self.insert_maintain(node, node.child[pos], pos)

    def insert_maintain(self, parent, child, pos):
        """
        插入调整
        :param parent: 失衡结点的父结点
        :param child: 可能发生失横的结点
        :param pos: 失橫结点在父结点中的编号
        :return:
        """
        if child.n < self.n:  # 未失横
            return parent
        # 1. 将child结点分割成两个结点
        split_pos = self.n // 2
        node1, node2 = self.split_node(child, split_pos)

        # 将split_pos处的关键字插入到parent结点去
        self.shift_1(parent.keys, pos, child.keys[split_pos])
        self.shift_1(parent.child, pos)
        parent.child[pos] = node1
        parent.child[pos+1] = node2
        parent.n += 1

        del child

        return parent

    def split_node(self, node, pos):
        """
        将一个结点分裂成两个
        :param node:
        :param pos: 分裂位置
        :return:
        """
        node1 = BTreeNode(pos)
        node2 = BTreeNode(self.n-1-pos)

        node1.keys = node.keys[0:pos]
        node1.child = node.child[0:pos+1]

        node2.keys = node.keys[pos+1:]
        node2.child = node.child[pos+1:]

        return node1, node2

    def shift_1(self, arr, pos, val=None):
        """
        将arr数组后pos位置开始，向后移动一位,且pos处的值为val
        :param arr:
        :param pos:
        :return:
        """
        arr.append(0)
        arr[pos+1:] = arr[pos:-1]
        if val is not None:
            arr[pos] = val

    def delete(self, k):
        pass
