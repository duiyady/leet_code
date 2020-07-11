# -*- coding:utf-8 -*-
# @Time: 2020/7/11 19:10
# @Author: duiya duiyady@163.com


def addBinary(a, b):
    if len(a) < len(b):
        a, b = b, a
    jin = 0
    result = [0]*len(a)
    for i in range(1, len(b)+1):
        tmp = int(a[-i]) + int(b[-i]) + jin
        jin = tmp // 2
        result[-i] = str(tmp % 2)
    for i in range(len(b)+1, len(a)+1):
        tmp = int(a[-i]) + jin
        jin = tmp // 2
        result[-i] = str(tmp % 2)
    if jin != 0:
        result.insert(0, "1")
    return "".join(result)

if __name__ == '__main__':
    print(addBinary(a="100", b="110010"))