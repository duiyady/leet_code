# -*- coding:utf-8 -*-
# @Time: 2019-09-15 23:11
# @Author: duiya duiyady@163.com


"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
"""


def longestPalindrome(s):
    max_start = 0
    max_end = 0

    if len(s) == 1:
        return s
    if len(s) == 0:
        return ""

    for i in range(len(s)):
        tmpa1, tmpb1, tmpa2, tmpb2 = 0, 0, 0, 0
        if i == 0:
            tmpa1, tmpb1 = 0, 0
            if s[i] == s[i + 1]:
                tmpa2, tmpb2 = 0, 1
        else:
            tmpa1, tmpb1 = i, i
            while tmpa1 >= 0 and tmpb1 <= len(s) - 1 and s[tmpa1] == s[tmpb1]:
                tmpa1 = tmpa1 - 1
                tmpb1 = tmpb1 + 1
            tmpa1 = tmpa1 + 1
            tmpb1 = tmpb1 - 1
            if i < len(s) - 1 and s[i] == s[i + 1]:
                tmpa2, tmpb2 = i, i + 1
                while tmpa2 >= 0 and tmpb2 <= len(s) - 1 and s[tmpa2] == s[tmpb2]:
                    tmpa2 = tmpa2 - 1
                    tmpb2 = tmpb2 + 1
                tmpa2 = tmpa2 + 1
                tmpb2 = tmpb2 - 1
        if (tmpb2 - tmpa2) > (tmpb1 - tmpa1):
            tmpa, tmpb = tmpa2, tmpb2
        elif (tmpb2 - tmpa2) < (tmpb1 - tmpa1):
            tmpa, tmpb = tmpa1, tmpb1
        else:
            if tmpa1 < tmpa2:
                tmpa, tmpb = tmpa1, tmpb1
            else:
                tmpa, tmpb = tmpa2, tmpb2

        if (tmpb - tmpa) > (max_end - max_start):
            max_start, max_end = tmpa, tmpb
        elif (tmpb - tmpa) == (max_end - max_start):
            if tmpa < max_start:
                max_start, max_end = tmpa, tmpb
        if max_end == len(s) - 1:
            break
    return s[max_start: max_end + 1]


if __name__ == '__main__':
    print(longestPalindrome('adffgacsgaf'))