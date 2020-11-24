# -*- coding:utf-8 -*-
# @Time: 2020/7/23 8:55
# @Author: duiya duiyady@163.com


"""
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。
格雷编码序列必须以 0 开头。
示例 1:
输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2
对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。
00 - 0
10 - 2
11 - 3
01 - 1
"""


def grayCode(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    result = [0, 1]
    for i in range(2, n+1):
        tmp = []
        for val in reversed(result):
            tmp.append(val+pow(2, i-1))
        result.extend(tmp)
    return result

if __name__ == '__main__':
    print(grayCode(2))