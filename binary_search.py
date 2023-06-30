# -*- coding:utf-8 -*-
__author__ = 'px'
""" 二分查找算法
主要考虑情况：
1. =target
2. >target
3. <target
4. 常规mid设计时，交界面是否有冲突

是否有冲突，主要看交界面，如arr = [1,1]
求第一个等于1的位置：交界面是下标为0和1时，设置mid=(left+right)//2，当left=right=mid，值为目标值，则返回
求最后一个等于1的位置：交界面是下标为0和1时，设置mid=(left+right+1)//2，当left=right=mid，值为目标值，则返回

"""


def binary_search(arr, num):
    """ [l, r] 左闭右闭"""
    l, r = 0, len(arr)-1

    while l <= r:
        mid = l + (r-l)//2

        if num > arr[mid]:
            l = mid + 1
        elif num == arr[mid]:
            return mid
        else:
            r = mid - 1
    return -1


def binary_search_first(arr, num):
    """
    寻找第一个等于num的位置
    [l, r] 左闭右闭
    """
    l, r = 0, len(arr)-1

    while l <= r:
        mid = l + (r-l)//2

        if num > arr[mid]:
            l = mid + 1
        elif num == arr[mid]:
            if l == r:
                return mid
            r = mid
        else:
            r = mid - 1
    return -1


def binary_search_last(arr, num):
    """
    寻找最后一个等于num的位置
    [l, r] 左闭右闭
    """
    l, r = 0, len(arr)-1

    while l <= r:
        mid = l + (r-l+1)//2

        if num > arr[mid]:
            l = mid + 1
        elif num == arr[mid]:
            if l == r:
                return mid
            l = mid
        else:
            r = mid - 1
    return -1


if __name__ == "__main__":
    # arr = [1,5,6,8,9,10]
    # res = binary_search(arr, 10)
    # print(res)
    arr1 = [0,1,1,1,1,1]
    res1 = binary_search_first(arr1, 1)
    print(res1)

    res2 = binary_search_last(arr1, 1)
    print("res2: ", res2)



