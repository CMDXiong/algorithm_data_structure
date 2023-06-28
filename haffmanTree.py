# -*- coding:utf-8 -*-
__author__ = 'px'
from linear_list.heap import Heap


class Node:
    def __init__(self, freq, ch, left=None, right=None):
        self.left = left
        self.right = right
        self.key = ch
        self.p = freq


def build_haffman_tree(arr):
    arr = [[it[0], it[1], Node(*it)] for it in arr]
    haffman_heap = Heap()
    haffman_heap.heapify(arr)
    n = len(arr)
    head = None
    for _ in range(1, n):
        res1 = haffman_heap.top()
        node1 = res1[2]
        haffman_heap.pop()

        res2 = haffman_heap.top()
        node2 = res2[2]
        haffman_heap.pop()

        head = Node(node1.p+node2.p, '0')
        head.left = node1
        head.right = node2
        haffman_heap.push([node1.p+node2.p, '0', head])

    return head


def output(head):
    from collections import deque
    st = deque()
    st.append(head)
    while st:
        tmp = []
        for _ in range(len(st)):
            node = st.popleft()
            tmp.append((node.p, node.key))
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        print(tmp)


if __name__ == "__main__":
    arr = [(0.5, 'a'), (0.2, 'b'), (0.2, 'd'), (0.1, 'c')]

    head = build_haffman_tree(arr)
    output(head)

