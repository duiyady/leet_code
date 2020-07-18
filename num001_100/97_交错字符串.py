# -*- coding:utf-8 -*-
# @Time: 2020/7/18 9:03
# @Author: duiya duiyady@163.com

"""
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
示例 1:
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
"""

def isInterleave2(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    i_1, i_2, i_3 = 0, 0, 0
    t_1, t_2, t_3, flag = [-1,], [-1, ], [-1,], 0

    while i_3 < len(s3) and i_3 != -1:
        if i_1 < len(s1) and i_2 < len(s2):
            if s1[i_1] == s2[i_2]:
                if s1[i_1] == s3[i_3]:
                    t_1.append(i_1)
                    t_2.append(i_2)
                    t_3.append(i_3 + 1)
                    i_3 += 1
                    i_1 += 1
                else:
                    i_1 = t_1.pop()
                    i_2 = t_2.pop() + 1
                    i_3 = t_3.pop()
            elif s1[i_1] == s3[i_3]:
                i_1 += 1
                i_3 += 1
            elif s2[i_2] == s3[i_3]:
                i_2 += 1
                i_3 += 1
            else:
                i_1 = t_1.pop()
                i_2 = t_2.pop() + 1
                i_3 = t_3.pop()
        elif i_1 < len(s1):
            if s1[i_1] == s3[i_3]:
                i_1 += 1
                i_3 += 1
            else:
                i_1 = t_1.pop()
                i_2 = t_2.pop() + 1
                i_3 = t_3.pop()
        else:
            if s2[i_2] == s3[i_3]:
                i_2 += 1
                i_3 += 1
            else:
                i_1 = t_1.pop()
                i_2 = t_2.pop() + 1
                i_3 = t_3.pop()
    if i_3 == -1:
        return False
    else:
        return True


def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False

    result = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    result[0][0] = 1
    for i in range(1, len(s2)+1):
        if s2[i-1] == s3[i-1]:
            result[0][i] = 1
        else:
            break
    for j in range(1, len(s1) + 1):
        if s1[j-1] == s3[j-1]:
            result[j][0] = 1
        else:
            break
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if result[i-1][j] == 1 and s1[i-1] == s3[i+j-1]:
                result[i][j] = 1
            elif result[i][j-1] == 1 and s2[j-1] == s3[i+j-1]:
                result[i][j] = 1
    return True if result[len(s1)][len(s2)] else False


if __name__ == '__main__':
    print(isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
    print(isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))



