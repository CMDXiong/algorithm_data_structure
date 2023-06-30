# -*- coding:utf-8 -*-
__author__ = 'px'

"""  快速排序 
1. 选取基准值
2. 分成大于基准值和小于基准值两部分
"""


def quick_sort(arr, l, r):
    if r - l <= 1:
        if r - l == 1 and arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return

    # partation
    p1, p2, z =l, r, arr[l]

    while p1 < p2:

        while p1 < p2 and arr[p2] >= z:
            p2 -= 1
        if p1 < p2:
            arr[p1] = arr[p2]
            p1 += 1

        while p1 < p2 and arr[p1] <= z:
            p1 += 1
        if p1 < p2:
            arr[p2] = arr[p1]
            p2 -= 1

    arr[p1] = z

    quick_sort(arr, l, p1)
    quick_sort(arr, p1+1, r)


if __name__ == "__main__":
    arr = [1,9,5,2,7,10,8]
    quick_sort(arr, 0, len(arr)-1)

    print(arr)

