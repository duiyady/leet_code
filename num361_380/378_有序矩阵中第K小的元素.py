# -*- coding:utf-8 -*-
# @Time: 2020/7/2 10:33
# @Author: duiya duiyady@163.com


"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
示例：
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
返回 13。
"""


def kthSmallest(matrix, k):
    now = [0]*len(matrix)
    for i in range(k):
        now_min = len(matrix)-1
        for j in range(len(matrix)):
            if now[j] < len(matrix):
                if matrix[j][now[j]] < matrix[now_min][now[now_min]]:
                    now_min = j
        now[now_min] += 1
    return matrix[now_min][now[now_min]-1]


if __name__ == '__main__':
    # print(kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))
    print(kthSmallest(matrix=[[1, 2], [1, 3]], k=1))