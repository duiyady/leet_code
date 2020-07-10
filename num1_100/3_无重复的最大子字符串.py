# -*- coding:utf-8 -*-
# @Time: 2019-09-15 23:07
# @Author: duiya duiyady@163.com


"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""


def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    max = 0
    dic = {}
    start = 0
    count = 0
    for s1 in s:
        if dic.get(s1) == None:
            now = count - start
            if now > max:
                max = now
            dic[s1] = count
        else:
            if dic.get(s1) >= start:
                now = count - dic.get(s1) - 1
                if now > max:
                    max = now
                start = dic.get(s1) + 1
                dic[s1] = count
            else:
                now = count - start
                if now > max:
                    max = now
                dic[s1] = count
        count = count + 1
    return max + 1


if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabcbb'))