# -*- coding:utf-8 -*-
__author__ = 'px'

""" 归并排序 """


def merge_sort(arr, l, r):
    """[l,r]"""
    if l == r:
        return None

    mid = l + (r-l)//2

    # 分治
    merge_sort(arr, l, mid)
    merge_sort(arr, mid+1, r)

    # 合并[l,mid], [mid+1, r]两个数组
    p1, p2 = l, mid+1

    tmp = []
    while p1 <= mid and p2 <= r:
        if arr[p1] < arr[p2]:
            tmp.append(arr[p1])
            p1 += 1
        else:
            tmp.append(arr[p2])
            p2 += 1

    while p1 <= mid:
        tmp.append(arr[p1])
        p1 += 1

    while p2 <= r:
        tmp.append(arr[p2])
        p2 += 1

    arr[l:r+1] = tmp


if __name__ == "__main__":
    arr = [1,9,5,2,7,10,8]
    merge_sort(arr, 0, len(arr)-1)

    print(arr)