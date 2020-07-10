# -*- coding:utf-8 -*-
# @Time: 2019-09-16 19:47
# @Author: duiya duiyady@163.com


def reverse(x):
    flag = 0  # 正数
    if x < 0:
        flag = 1  # 负数
    x = abs(x)
    result = 0
    max_v = pow(2, 31)-1
    min_v = -pow(2, 31)
    while x > 0:
        result = result*10 + x%10
        x = x // 10
    if flag == 1:
        result = -result
    if result > max_v or result < min_v:
        return 0
    return result


if __name__ == '__main__':
    print(reverse(-153423646))