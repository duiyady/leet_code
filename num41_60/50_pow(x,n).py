# -*- coding:utf-8 -*-
# @Time: 2020/7/2 19:43
# @Author: duiya duiyady@163.com


def myPow(x, n):
    now = x
    result = 1.0
    n_tmp = abs(n)
    if n == 0:
        return 1
    while n_tmp > 1:
        t = n_tmp%2
        if t == 1:
            result = result*now
        n_tmp = n_tmp//2
        now = now*now
    result = result*now
    if n < 0:
        result = 1/result
    return result


if __name__ == '__main__':
    print(myPow(2, 11))