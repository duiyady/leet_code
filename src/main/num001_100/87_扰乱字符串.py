# -*- coding:utf-8 -*-
# @Time: 2020/7/30 21:57
# @Author: duiya duiyady@163.com


"""
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
下图是字符串 s1 = "great" 的一种可能的表示形式。
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。
例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
我们将 "rgeat” 称作 "great" 的一个扰乱字符串。
同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
我们将 "rgtae” 称作 "great" 的一个扰乱字符串。
给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。

示例 1:
输入: s1 = "great", s2 = "rgeat"
输出: true

示例 2:
输入: s1 = "abcde", s2 = "caebd"
输出: false
"""

def isScramble(s1, s2):
    if s1 == s2:
        return True
    s_len = len(s1)
    flag_array = [[[False]*(s_len+1) for _ in range(s_len)] for _2 in range(s_len)]

    for i in range(s_len):
        for j in range(s_len):
            if s1[i] == s2[j]:
                flag_array[i][j][1] = True
    for length in range(2, s_len+1):
        for i in range(s_len - length + 1):
            for j in range(s_len - length + 1):
                for k in range(1, length):
                    if flag_array[i][j][k] and flag_array[i + k][j + k][length - k]:
                        flag_array[i][j][length] = True
                        break
                    if flag_array[i][j + length - k][k] and flag_array[i + k][j][length - k]:
                        flag_array[i][j][length] = True
                        break
    return flag_array[0][0][s_len]


def isScramble2(s1, s2):
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False

    for i in range(1, len(s1)):
        if isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]) or \
                (isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i])):
            return True
    return False






if __name__ == '__main__':
    print(isScramble(s1 = "abc", s2 = "cab"))
