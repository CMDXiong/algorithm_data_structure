# -*- coding:utf-8 -*-
__author__ = 'px'


def bubble_sort(arr):
    n = len(arr)

    for i in range(1, n):
        for j in range(0, n-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]


if __name__ == "__main__":
    arr = [1,9,5,2,7,10,8, 9]
    bubble_sort(arr)

    print(arr)