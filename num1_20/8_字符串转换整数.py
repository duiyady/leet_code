# -*- coding:utf-8 -*-
# @Time: 2019-09-16 20:08
# @Author: duiya duiyady@163.com


def myAtoi(str):
    max_v = pow(2, 31) - 1
    min_v = -pow(2, 31)
    flag = 0  # 表示还没有遇到数字 1正数 2负数
    result = 0
    for ch in str:
        if flag == 0:
            if ch == '+':
                flag = 1
            elif ch == '-':
                flag = 2
            elif '9' >= ch >= '0':
                result = result*10 + int(ch)
                flag = 1
            elif ch == ' ':
                continue
            else:
                break
        else:
            if '9' >= ch >= '0':
                result = result * 10 + int(ch)
            else:
                break
    if flag == 2:
        result = -result
    if result > max_v:
        return max_v
    elif result < min_v:
        return min_v
    else:
        return result


if __name__ == '__main__':
    print(myAtoi('   -123'))
