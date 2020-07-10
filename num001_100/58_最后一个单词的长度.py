# -*- coding:utf-8 -*-
# @Time: 2020/7/7 22:07
# @Author: duiya duiyady@163.com


"""
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
如果不存在最后一个单词，请返回 0。
说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。
"""


def lengthOfLastWord(s):
    end = len(s) - 1
    while end >= 0 and s[end] == " ":
        end -= 1
    if end < 0:
        return 0
    start = end
    while start >= 0 and s[start] != " ":
        start -= 1
    return end-start


if __name__ == '__main__':
    print(lengthOfLastWord(" Hello  "))



