# -*- coding:utf-8 -*-
# @Time: 2020/7/20 16:56
# @Author: duiya duiyady@163.com

"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
示例:
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

def combine(n, k):
    result = []
    tmp = []
    def fun(i, last):
        if i == k:
            result.append(tmp.copy())
            return
        for va in range(last+1, n + 1):
            tmp.append(va)
            fun(i+1, va)
            tmp.pop()
        return
    fun(0, 0)
    return result


if __name__ == '__main__':
    print(combine(n=4, k=2))
