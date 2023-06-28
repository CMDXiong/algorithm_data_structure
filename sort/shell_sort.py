# -*- coding:utf-8 -*-
__author__ = 'px'
"""
1. 设计一个步长
2. 按照步长，对序列进行分组，每组采用插入排序
3. 直到执行步长为1为止

参考时间复杂度：O(nlogn)~O(n2)
"""


def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j, num = i-1, arr[i]
        while j >= 0 and num < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = num

    return arr

def shell_sort(arr):
    pass