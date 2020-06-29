# -*- coding:utf-8 -*-
# @Time: 2020/6/29 15:01
# @Author: duiya duiyady@163.com


"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
示例 1:
输入: num1 = "123", num2 = "456"
输出: "56088"
说明：
num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""


def multiply(num1, num2):
    if num2 == "0" or num1 == "0":
        return "0"
    result = [0]*(len(num1) + len(num2))
    for i in range(1, len(num1)+1):
        for j in range(1, len(num2)+1):
            val = int(num1[-i])*int(num2[-j]) + result[-(i+j-1)]
            result[-(i+j-1)] = val%10
            result[-(i+j)] += val//10
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    return "".join([str(x) for x in result])


if __name__ == '__main__':
    print(multiply("999", "988"))
