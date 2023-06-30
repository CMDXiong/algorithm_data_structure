# -*- coding:utf-8 -*-
__author__ = 'px'

""" 单调递增栈：栈顶是最大的
求解每个元素右则离它最近且小于它的元素
和左则离它最近且小于它的元素
"""


if __name__ == "__main__":
    st = []

    arr = [-1, 3, 1, 4, 5, 2, 9, 8, 12, -1]

    l = [None] * (len(arr)-1)
    r = [None] * (len(arr)-1)

    # right 求解每个元素右则离它最近且小于它的元素: 单调递增栈
    for i in range(len(arr)-1):
        while st and arr[st[-1]] > arr[i]:
            r[st[-1]] = i
            st.pop()
        st.append(i)

    # left 求解每个元素左则离它最近且小于它的元素: 单调递增栈
    st2 = []
    for j in range(len(arr)-1, -1, -1):
        while st2 and arr[st2[-1]] > arr[j]:
            l[st2[-1]] = j
            st2.pop()
        st2.append(j)

    print("r: ", r)
    print("l: ", l)


