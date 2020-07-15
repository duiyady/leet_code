# -*- coding:utf-8 -*-
# @Time: 2020/7/15 21:33
# @Author: duiya duiyady@163.com


"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
"""


def climbStairs(n):
    result = [1]*(n+1)
    for i in range(2, n+1):
        result[i] = result[i-1] + result[i-2]
    return result[n]

if __name__ == '__main__':
    print(climbStairs(3))