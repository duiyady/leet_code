# -*- coding:utf-8 -*-
# @Time: 2020/7/17 19:39
# @Author: duiya duiyady@163.com


"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
"""


def searchMatrix(matrix, target):
    if len(matrix) == 0:
        return False
    if len(matrix[0]) == 0:
        return False
    index = 0
    while index < len(matrix):
        if matrix[index][0] <= target:
            index += 1
        else:
            break
    index -= 1
    for i in range(len(matrix[0])):
        if matrix[index][i] == target:
            return True
        if matrix[index][i] > target:
            return False
    return False