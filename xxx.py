# -*- coding:utf-8 -*-
__author__ = 'px'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def validateStackSequences(pushed, popped) -> bool:
    stack = []
    j = 0
    for num in pushed:
        stack.append(num)
        while stack and num == stack[-1]:
            stack.pop()
            popped.pop()

    return len(stack) == 0


print(validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))