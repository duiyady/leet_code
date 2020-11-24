# -*- coding:utf-8 -*-
# @Time: 2020/7/26 11:03
# @Author: duiya duiyady@163.com

"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
示例:
输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
"""


def maximalRectangle(matrix):
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])

    left = [0] * n
    right = [n] * n
    height = [0] * n

    maxarea = 0

    for i in range(m):
        cur_left, cur_right = 0, n
        # update height
        for j in range(n):
            if matrix[i][j] == '1':
                height[j] += 1
            else:
                height[j] = 0
        # update left
        for j in range(n):
            if matrix[i][j] == '1':
                left[j] = max(left[j], cur_left)
            else:
                left[j] = 0
                cur_left = j + 1
        # update right
        for j in range(n - 1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], cur_right)
            else:
                right[j] = n
                cur_right = j
        # update the area
        for j in range(n):
            maxarea = max(maxarea, height[j] * (right[j] - left[j]))
    return maxarea

if __name__ == '__main__':
    print(maximalRectangle([["1","0","1","0","0"],
                            ["1","0","1","1","1"],
                            ["1","1","1","1","1"],
                            ["1","0","0","1","0"]]))