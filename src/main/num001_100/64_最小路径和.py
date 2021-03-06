# -*- coding:utf-8 -*-
# @Time: 2020/7/10 5:07 下午
# @Author: duiya duiyady@163.com

"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""

def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    for i in reversed(range(m)):
        for j in reversed(range(n)):
            if j+1 < n and i+1 < m:
                grid[i][j] += min(grid[i][j+1], grid[i+1][j])
            elif j+1 < n:
                grid[i][j] += grid[i][j + 1]
            elif i+1 < m:
                grid[i][j] += grid[i+1][j]
    return grid[0][0]

if __name__ == '__main__':
    print(minPathSum([[1, 3, 1],
                      [1, 5, 1],
                      [4, 2, 1]]))

    print(minPathSum([[1, 3, 1],]))


