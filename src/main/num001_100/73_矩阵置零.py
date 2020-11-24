# -*- coding:utf-8 -*-
# @Time: 2020/7/17 19:23
# @Author: duiya duiyady@163.com


"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
"""


def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    row = set()
    col = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
    for va in row:
        for i in range(len(matrix[0])):
            matrix[va][i] = 0
    for va in col:
        for i in range(len(matrix)):
            matrix[i][va] = 0




