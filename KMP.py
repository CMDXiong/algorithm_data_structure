# -*- coding:utf-8 -*-
__author__ = 'px'

"""
判断一个字符串pattern，是否在另一个字符串text中
pattern = "ABACABAB"
next = [0, 0, 1, 0, 1, 2, 3, 2]
next[i]: 代表【0...i】之间的最长公共前后缀

next的构建:
1. 首先比较当前字符与当前最长公共前后缀对应的值是否相同
    如i = 7时，当前当前最长公共前后缀对应prefix_len是3，而比较的是pattern[7]与pattern[3]是否相等，
    1. 相等，则next[7] = prefix_len + 1
    2. 不相等，则修改prefix_len = next[prefix_len-1],在进行比较，直到prefix_len为0或者再次相等

参考视频链接: https://www.bilibili.com/video/BV1AY4y157yL/?spm_id_from=333.337.search-card.all.click&vd_source=e25e7f46fef91ff676e3f70e6413ebf2
"""


def build_next(pattern):
    # 构建next数组
    prefix_len = 0  # 当前最长公共前后缀长度

    next = [0]
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[prefix_len]:
            prefix_len += 1
            next.append(prefix_len)
            i += 1
        else:
            if prefix_len == 0:
                next.append(0)
                i += 1
            else:
                prefix_len = next[prefix_len-1]
    return next


def kmp(text, pattern):
    next = build_next(pattern)

    text_len = len(text)

    j = 0
    p_len = len(pattern)

    for i in range(text_len):
        while j > 0 and text[i] != pattern[j]:
            j = next[j]

        if text[i] == pattern[j]:
            j += 1
            if j == p_len:
                return i-p_len+1

    return -1


if __name__ == '__main__':
    pattern = "ABACABAB"
    print(build_next(pattern))

    text = "bacbababadababacambabacaddababacasdsd"
    pattern = "ababaca"

    res = kmp(text, pattern)
    print(text[res:res + len(pattern)] == pattern)





