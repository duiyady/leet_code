# -*- encoding:utf-8 -*-
# @Time: 2019/10/25 14:00
# @Author duiya duiyady@163.com

"""
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
"""

def strStr(haystack, needle):
    if len(haystack) == 0:
        if len(needle) != 0:
            return -1
        else:
            return 0
    if len(needle) == 0:
        return 0

    def get_match(arra):
        max_match = [None] * len(arra)
        max_match[0] = 0
        maxlen = 0
        for i in range(1, len(arra)):
            while maxlen > 0 and arra[maxlen] != arra[i]:
                maxlen = max_match[maxlen - 1]
            if arra[i] == arra[maxlen]:
                maxlen += 1
            max_match[i] = maxlen
        return max_match

    max_match = get_match(needle)
    i, j = 0, 0
    while i < len(haystack) and j < len(needle):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = max_match[j - 1]
    if j == len(needle):
        return i - j
    else:
        return -1

if __name__ == '__main__':
    print(strStr('hello', 'll'))