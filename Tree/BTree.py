# -*- coding:utf-8 -*-
__author__ = 'px'

"""
索引为何不用散列来做？
    1. 哈希函数设计索引，会存在哈希冲突，导致散列不均匀，存在大量的线性查找
    2. 在范围查找时，会退化成线性查找，hash不合适
    3. 优点是等值查询比较快 
"""
from random import sample, seed


class BTreeNode:
    def __init__(self, leaf=False):
        """
        keys数组中i个key，左边孩子为child[i],右边孩子为child[i+1]
        :param leaf: 叶子结点标记
        """
        self.keys = []      # 包含的关键字
        self.children = []  # 结点的孩子
        self.leaf = leaf

    def left(self, i):
        """ 第i个关键字的左子树"""
        return self.children[i]

    def right(self, i):
        """ 第i个关键字的右子树"""
        if i < self.n:
            return self.children[i+1]
        return None

    def shift_keys(self, start=0, bits=1, val=None):
        """ 将keys数组开start开向后移动bits位, 并填充val"""
        self.keys = self.keys[0:start] + [val]*bits + self.keys[start:]

    def shift_children(self, start=0, bits=1, val=None):
        self.children = self.children[0:start] + [val] * bits + self.children[start:]

    @property
    def n(self):
        # 关键字的个数
        return len(self.keys)


class BTree:
    def __init__(self, m, root=None):
        self.m = m  # m阶B树，即最多个m个孩子
        self.n = self.m - 1  # 最多有n个关键字
        self.min_n = (self.m+1) // 2 - 1  # 最少需要的关键字数量

        self.root = root

    def search(self, key, node=None):
        if node is None:
            return self.search(key, self.root)

        if node.leaf:  # 叶子结点
            return None

        i = self._pos(node, key)

        # 找到
        if i < node.n and key == node.keys[i]:
            return node, i
        else:
            if not node.children:
                return None
            return self.search(key, node.children[i])

    def _pos(self, root, key):
        """
        找到 key 所属root的孩子的位置(即第一个大于等于key的位置pos)
        1. root.keys[pos] <= key < root.keys[pos+1]
        2. 位于root的孩子指针: root.child[pos]
        """
        pos = 0
        while pos < root.n and key > root.keys[pos]:
            pos += 1
        return pos

    def insert(self, key):
        self.root = self.aux_insert(self.root, key)

    def aux_insert(self, root, key):
        # 进行插入后，带回来的根root的节点个数可能超出范围，需要进行插入调整
        root = self._insert(root, key)

        # root 关键字数量超过了最大值
        if root.n == self.m:
            p = BTreeNode()
            p.children.append(root)
            # 失衡调整
            root = self.insert_maintain(p, root, 0)

        return root

    def _insert(self, root, key):
        # root为空或为终端结点
        if root is None or (not root.children):
            return self.insert_key(root, key)

        pos = self._pos(root, key)  # >=key的位置
        if pos < root.n and key == root.keys[pos]:  # key 在root中
            return root

        self._insert(root.children[pos], key)  # 向子孩子中继续查找插入
        return self.insert_maintain(root, root.children[pos], pos)

    def insert_maintain(self, parent, child, pos):
        """
        插入调整: 当结点关键字数量大到n时，引发插入调整
        插入调整的核心操作是: 节点分裂
        :param parent: 失衡结点的父结点
        :param child: 可能发生失横的结点
        :param pos: 失橫结点在父结点中的编号
        :return:
        """
        if child.n < self.m:  # 未失横
            return parent

        # 1. 将child结点分割成两个结点
        split_pos = self.m // 2
        node1, node2 = self.split_node(child, split_pos)

        key = child.keys[split_pos]  # 分裂点的key值

        # 将split_pos处的关键字插入到parent结点去
        parent.keys.insert(pos, key)

        parent.children.insert(pos, node1)
        parent.children[pos+1] = node2

        return parent

    def insert_key(self, node, key):
        """
        将key插入到node, keys，此时并不考虑node是否满足B树结点条件
        :param node:
        :param key:
        :return:
        """
        if node is None:
            node = BTreeNode()
            node.keys.append(key)
            return node

        pos = self._pos(node, key)  # >=key的位置

        if pos < node.n and node.keys[pos] == key:  # key 存在于node中
            return node

        node.keys.insert(pos, key)  # key不存在于node中
        return node

    def split_node(self, node, pos):
        """
        将一个结点分裂成两个
        :param node:
        :param pos: 分裂位置
        :return:
        """
        node1 = BTreeNode()
        node2 = BTreeNode()

        node1.keys = node.keys[0:pos]
        node1.children = node.children[0:pos + 1]

        node2.keys = node.keys[pos+1:]
        node2.children = node.children[pos + 1:]

        return node1, node2

    def delete(self, key):
        root = self._delete(self.root, key)
        if root.n == 0:
            root = root.children[0]
        self.root = root

    def _delete(self, root, key):
        """
        删除操作
        """
        if root is None:
            return root

        # root是终端结节
        if not root.children:
            if key in root.keys:
                root.keys.remove(key)
            return root
        else:  # root是非终端结节
            pos = self._pos(root, key)
            if pos < root.n and root.keys[pos] == key:
                tmp = self.predecessor(root, key)
                root.keys[pos] = tmp.keys[-1]

                root.children[pos] = self._delete(root.children[pos], tmp.keys[-1])
            else:
                root.children[pos] = self._delete(root.children[pos], key)

        root = self.delete_maintain(root, pos)
        return root

    def delete_maintain(self, root, pos):
        """
        删除调整: 发生在节点关键字数量为: self.min_n -1时
        操心操作：左旋，右旋，合并
        1. 右旋：向左边兄弟借
        2. 左旋：向右边兄弟借
        3. 合并：与兄弟，以及兄弟和自己对应的父节点的那个关键字，进行合并
        :param root:
        :param pos: 待检查的分支
        :return:
        """
        if root.children[pos].n >= self.min_n:
            return root

        # 1. 向左边兄弟借
        if pos > 0 and root.children[pos-1].n > self.min_n:
            self.right_rotate(root, pos-1)

        # 2. 向右边兄弟借
        elif pos < root.n and root.children[pos+1].n > self.min_n:
            self.left_rotate(root, pos)

        # 3. 合并
        else:
            if pos > 0:
                self.merge(root, pos-1)
            else:
                self.merge(root, pos)

        return root

    def left_rotate(self, root, pos):
        """ 左旋 """
        r_child = root.right(pos)
        l_child = root.left(pos)

        l_child.keys.append(root.keys[pos])
        root.keys[pos] = r_child.keys.pop(0)

        # r_child是终端结点时，r_child.children为空
        if len(r_child.children):
            l_child.children.append(r_child.children.pop(0))

    def right_rotate(self, root, pos):
        """
        右旋：向左孩子借
        将pos位置的值借给pos+1位置
        """
        r_child = root.right(pos)
        l_child = root.left(pos)

        r_child.shift_keys(start=0, bits=1, val=root.keys[pos])
        root.keys[pos] = l_child.keys.pop()

        # l_child是终端结点时，r_child.children为空
        if len(l_child.children):
            r_child.shift_children(start=0, bits=1, val=l_child.children.pop())

    def merge(self, root, pos):
        """ 合并 root中 第pos和pos+1的两条分支"""
        l_child = root.left(pos)
        r_child = root.right(pos)
        root_key = root.keys.pop(pos)

        new_node = BTreeNode()
        new_node.keys = l_child.keys + [root_key] + r_child.keys
        new_node.children = l_child.children + r_child.children

        root.children[pos] = new_node

    def predecessor(self, root, key):
        pos = self._pos(root, key)
        tmp = root.children[pos]
        while tmp.children:
            tmp = tmp.children[-1]
        return tmp


def output(root):
    if root is None:
        return
    print_node(root)
    for child in root.children:
        output(child)


def print_node(root):
    print_str = "{}: {}".format(root.n, root.keys)

    for child in root.children:
        print_str += " " + str(child.keys[0])

    print(print_str)


if __name__ == "__main__":
    MAX_OP = 12

    seed(666)

    b_tree = BTree(3)

    nums = sample(range(1, 100), MAX_OP)
    print(nums)

    for num in nums:
        print("insert {} to BTree".format(num))
        b_tree.insert(num)
        output(b_tree.root)

    print("search: ", b_tree.search(92))

    while True:
        x = input("输入一个数: ")
        if x == 'q':
            break
        x = int(x)
        print("delete {} from B Tree: ".format(x))
        b_tree.delete(x)
        output(b_tree.root)

