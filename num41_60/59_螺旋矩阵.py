# -*- coding:utf-8 -*-
# @Time: 2020/7/8 17:14
# @Author: duiya duiyady@163.com

"""
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

def generateMatrix(n):
    result = [[0 for i in range(n)] for i in range(n)]
    count = 1
    for i in range((n+1)//2):
        for j in range(i, n-i):
            result[i][j] = count
            count += 1
        for j in range(i+1, n-i):
            result[j][n-i-1] = count
            count += 1
        if n - i - 1 != i:
            for j in reversed(range(i, n-i-1)):
                result[n-i-1][j] = count
                count += 1
            for j in reversed(range(i+1, n-i-1)):
                result[j][i] = count
                count += 1
    return result


if __name__ == '__main__':
    print(generateMatrix(4))