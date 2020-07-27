# -*- coding:utf-8 -*-
# @Time: 2020/7/27 10:51
# @Author: duiya duiyady@163.com


"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"
返回 true.

示例 2:
s = "axc", t = "ahbgdc"
返回 false.
"""

def isSubsequence(s, t):
    if len(s) == 0:
        return True
    char_index = dict()
    flag = dict()
    for i in range(len(s)):
        if s[i] in char_index.keys():
            char_index[s[i]].append(i)
        else:
            char_index[s[i]] = [i]
        flag[i] = []

    for i in range(len(t)):
        if t[i] in char_index.keys():
            now_index = char_index[t[i]]
            for now in now_index:
                end_flag = False
                if now == 0:
                    flag[0].append(i)
                    end_flag = True
                else:
                    choices = flag[now-1]
                    for va in choices:
                        if va < i:
                            flag[now].append(i)
                            end_flag = True
                            break
                if now == len(s)-1 and end_flag:
                    return True
    return False

if __name__ == '__main__':
    print(isSubsequence(s="aaaaaa", t="bbaaaa"))


