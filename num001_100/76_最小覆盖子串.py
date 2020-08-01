# -*- coding:utf-8 -*-
# @Time: 2020/7/27 20:25
# @Author: duiya duiyady@163.com


"""
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
"""

def minWindow(s, t):
    if len(t) > len(s):
        return ""
    if s == t:
        return t
    char_count = {}
    for i in range(len(t)):
        if t[i] in char_count.keys():
            char_count[t[i]] += 1
        else:
            char_count[t[i]] = 1
    start = 0
    min_s, min_e = 0, 99999999999999
    change = False
    now_count = {}
    for k, v in char_count.items():
        now_count[k] = 0
    for i in range(len(s)):
        if s[i] in char_count.keys():
            now_count[s[i]] += 1
        flag = True
        for k in char_count.keys():
            if now_count[k] < char_count[k]:
                flag = False
                break
        if flag:
            while True:
                if s[start] not in char_count.keys():
                    start += 1
                else:
                    if now_count[s[start]]-1 >= char_count[s[start]]:
                        now_count[s[start]] -= 1
                        start += 1
                    else:
                        break
            if (i - start) < (min_e - min_s):
                change = True
                min_s, min_e = start, i
            now_count[s[start]] -= 1
            start += 1
    if change:
        return s[min_s: min_e+1]
    else:
        return ""




if __name__ == '__main__':
    print(minWindow(s="abc", t="cba"))
