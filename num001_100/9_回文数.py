# -*- coding:utf-8 -*-
# @Time: 2019-09-16 20:20
# @Author: duiya duiyady@163.com


def isPalindrome(x):
    if x < 0:
        return False
    x = str(x)
    i, j = 0, len(x)-1
    while i < j:
        if x[i] == x[j]:
            i = i + 1
            j = j - 1
        else:
            break
    if i < j:
        return False
    else:
        return True


if __name__ == '__main__':
    print(isPalindrome(123))