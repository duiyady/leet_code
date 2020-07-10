# -*- coding:utf-8 -*-
# @Time: 2020/7/4 15:57
# @Author: duiya duiyady@163.com


"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
"""


def spiralOrder(matrix):
    result = []
    row_end = len(matrix)-1
    col_end = len(matrix[0])-1
    for i in range((min(row_end, col_end)+2)//2):
        print("开始", i)
        for j in range(i, col_end-i+1):
            result.append(matrix[i][j])
            print(0, i, j)
        for j in range(i+1, row_end-i+1):
            result.append(matrix[j][col_end-i])
            print(1, j, col_end-i)
        if row_end-i != i:
            for j in reversed(range(i, col_end-i)):
                result.append(matrix[row_end-i][j])
                print(2, row_end-i, j)
        if col_end-i != i:
            for j in reversed(range(i+1, row_end-i)):
                result.append(matrix[j][i])
                print(3, j, i)
    return result


if __name__ == '__main__':
    print(spiralOrder(matrix=[[7],[9],[6]]))