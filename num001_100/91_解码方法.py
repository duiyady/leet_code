# -*- coding:utf-8 -*-
# @Time: 2020/8/9 9:35
# @Author: duiya duiyady@163.com


"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：
'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:
输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

示例 2:
输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
"""


def numDecodings(s):
    if len(s) == 0:
        return 0
    if s[0] == "0":
        return 0
    count = [0]*(len(s)+1)
    count[0] = 1
    count[1] = 1
    for i in range(1, len(s)):
        if s[i] != "0":
            count[i+1] = count[i]
        tmp = int(s[i-1: i+1])
        if tmp <= 26 and tmp >= 10:
            count[i+1] += count[i-1]
        elif tmp == 0:
            break
    return count[len(s)]

print(numDecodings("100"))

