# -*- coding:utf-8 -*-
__author__ = 'px'

"""
选择排序
每一轮选择一个最小的值放入

时间复杂度O(n2)
空间复杂度O(1)
"""

from random import sample


def selection_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        ind = i
        for j in range(i+1, n):
            if arr[ind] > arr[j]:
                ind = j
        arr[i], arr[ind] = arr[ind], arr[i]
    return arr


def check(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            print("The ordering is wrong")
            return False
    print("The ordering is correct")
    return True


if __name__ == "__main__":
    nums = sample(range(1, 1000), 10)
    print("before sort: ", nums)
    selection_sort(nums)
    print("after sort: ", nums)

    check(nums)



