# -*- coding:utf-8 -*-
# @Time: 2020/7/8 18:20
# @Author: duiya duiyady@163.com


"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。
说明：
给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:
输入: n = 3, k = 3
输出: "213"
"""

def getPermutation(n, k):
    nums = [str(i) for i in range(1, n + 1)]
    result = []
    tmp1 = n
    tmp = 1
    while tmp1 > 0:
        tmp = tmp * tmp1
        tmp1 -= 1
    k = k - 1
    for i in range(n):
        tmp = tmp // (n - i)
        index = k // tmp
        k = k % tmp
        result.append(nums.pop(index))
    return "".join(result)



if __name__ == '__main__':
    print(getPermutation(4, 9))
