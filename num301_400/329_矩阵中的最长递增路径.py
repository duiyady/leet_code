# -*- coding:utf-8 -*-
# @Time: 2020/7/26 9:19
# @Author: duiya duiyady@163.com


"""
给定一个整数矩阵，找出最长递增路径的长度。
对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
示例 1:
输入: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
输出: 4
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:
输入: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
输出: 4
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
"""


def longestIncreasingPath(matrix):
    if len(matrix) == 0:
        return 0
    n, m = len(matrix), len(matrix[0])
    tmp = [[0]*m for _ in range(n)]
    result = 0
    def huishuo(i, j):
        if tmp[i][j] == 0:
            tmp_count = [0]
            if i+1 < n and matrix[i+1][j] > matrix[i][j]:
                tmp_count.append(huishuo(i+1, j))
            if i-1 >= 0 and matrix[i-1][j] > matrix[i][j]:
                tmp_count.append(huishuo(i-1, j))
            if j+1 < m and matrix[i][j+1] > matrix[i][j]:
                tmp_count.append(huishuo(i, j+1))
            if j-1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                tmp_count.append(huishuo(i, j-1))
            tmp[i][j] = max(tmp_count)+1
        return tmp[i][j]

    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                huishuo(i, j)
                result = max(result, tmp[i][j])
    return result

if __name__ == '__main__':
    print(longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))