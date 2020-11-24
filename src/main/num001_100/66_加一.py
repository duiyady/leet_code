# -*- coding:utf-8 -*-
# @Time: 2020/7/11 16:27
# @Author: duiya duiyady@163.com


"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
"""

def plusOne(digits):
    jin = 1
    for i in reversed(range(len(digits))):
        digits[i] = digits[i]+jin
        jin = digits[i] // 10
        digits[i] = digits[i] % 10
    if jin != 0:
        digits.insert(0, jin)
    return digits

if __name__ == '__main__':
    print(plusOne([1,2,3]))