# -*- coding:utf-8 -*-
# @Time: 2020/7/1 10:40 下午
# @Author: duiya duiyady@163.com


"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
示例：
输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
"""

def findLength(A, B):
    if len(A) < len(B):
        A, B = B, A
    for i in range(len(B)):
        A.insert(0, "T")
    max_len = 0
    for i in range(0, len(A)):
        now_max = 0
        for j in range(i, min(len(A), i+len(B))):
            if A[j] == B[j-i]:
                now_max += 1
            else:
                if now_max > max_len:
                    max_len = now_max
                now_max = 0
        if now_max > max_len:
            max_len = now_max
    return max_len

if __name__ == '__main__':
    print(findLength(A=[0,0,0,0,1], B=[1,0,0,0,0]))