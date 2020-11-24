# -*- coding:utf-8 -*-
# @Time: 2020/7/30 15:33
# @Author: duiya duiyady@163.com


"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。

示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
"""

def integerBreak(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    result = [0, 1, 2, 3, 4, 6, 7, 12, 18, 27, 36]
    if n <= 10:
        return result[n]
    for i in range(11, n+1):
        now_max = 0
        for j in range(2, len(result)):
            tmp_max = j*result[-j]
            if tmp_max > now_max:
                now_max = tmp_max
            else:
                result.append(now_max)
                break
    return result[-1]


if __name__ == '__main__':
    print(integerBreak(14))