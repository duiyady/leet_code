# -*- coding:utf-8 -*-
# @Time: 2020/7/11 22:06
# @Author: duiya duiyady@163.com


"""
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去
"""

def mySqrt(x):
    start = 0
    end = x
    while start <= end:
        mid = (start + end) // 2
        if mid * mid <= x:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans


if __name__ == '__main__':
    print(mySqrt(8))