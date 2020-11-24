# -*- coding:utf-8 -*-
# @Time: 2020/8/3 9:58
# @Author: duiya duiyady@163.com


"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：
num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""

def addStrings(num1, num2):
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    result = [0]*(len(num1)+1)
    jia = 0
    for i in range(1, len(num2)+1):
        tmp = int(num2[-i]) + int(num1[-i]) + jia
        result[-i] = str(tmp%10)
        jia = tmp//10
    for i in range(len(num2)+1, len(num1)+1):
        tmp = int(num1[-i]) + jia
        result[-i] = str(tmp % 10)
        jia = tmp // 10
    if jia !=0:
        result[0] = str(jia)
    else:
        result.pop(0)
    return "".join(result)


if __name__ == '__main__':
    print(addStrings("123", "345"))
