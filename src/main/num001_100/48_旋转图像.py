# -*- coding:utf-8 -*-
# @Time: 2020/7/2 18:43
# @Author: duiya duiyady@163.com


"""
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
"""


def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    mat_len = len(matrix)-1
    for i in range((mat_len+1)//2):
        for j in range(i, mat_len - i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[mat_len - j][i]
            matrix[mat_len - j][i] = matrix[mat_len - i][mat_len - j]
            matrix[mat_len - i][mat_len - j] = matrix[j][mat_len - i]
            matrix[j][mat_len - i] = tmp


if __name__ == '__main__':
    rotate(matrix=[[1,2,3],[4,5,6],[7,8,9]])