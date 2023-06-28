# -*- coding:utf-8 -*-
__author__ = 'px'

"""
选择排序
每一轮选择一个最小的值放入

时间复杂度O(n2)
空间复杂度O(1)
"""

from random import sample
import time


def unguarded_insert_sort(arr):
    n = len(arr)
    ind = 0
    for i in range(1, n):
        if arr[i] < arr[ind]:
            ind = i

    # 保证插入排序的稳定性，不能直接交换ind和0位置的值
    while ind > 0:
        arr[ind], arr[ind-1] = arr[ind-1], arr[ind]
        ind -= 1

    for i in range(1, n):
        j = i
        while arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1


def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j, num = i-1, arr[i]
        while j >= 0 and num < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = num

    return arr


def check(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i-1] >= arr[i]:
            print("The ordering is wrong")
            return False
    print("The ordering is correct")
    return True


if __name__ == "__main__":
    nums = sample(range(1, 100), 10)
    print("before sort: ", nums)
    start = time.time()
    for _ in range(5000):
        insert_sort(nums)
    print("insert_sort: ", (time.time() - start)*1000, "ms")
    print("after sort: ", nums)

    start = time.time()
    for _ in range(5000):
        unguarded_insert_sort(nums)
    print("unguarded_insert_sort: ", (time.time() - start) * 1000, "ms")

    check(nums)



