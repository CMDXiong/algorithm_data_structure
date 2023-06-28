# -*- coding:utf-8 -*-
__author__ = 'px'
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists):
        nodes = lists

        heapq.heapify(nodes)
        dummy = ListNode()
        head = ListNode()
        dummy.next = head
        while nodes:
            node = heapq.heappop(nodes)

            head.next = node
            head = node
            if node.next:
                heapq.heappush(nodes, node.next)

        return dummy.next.next


def mergeKLists(lists):
    nodes = lists

    heapq.heapify(nodes)
    dummy = ListNode()
    head = ListNode()
    dummy.next = head
    while nodes:
        node = heapq.heappop(nodes)

        head.next = node
        head = node
        if node.next:
            heapq.heappush(nodes, node.next)

    return dummy.next.next


def output(head):
    while head:
        print(head.val)
        head = head.next


head1 = ListNode(1, ListNode(4, ListNode(5)))
head2 = ListNode(1, ListNode(3, ListNode(4)))
head3 = ListNode(2, ListNode(6))

lists = [head1, head2, head3]

res = mergeKLists(lists)

output(res)

