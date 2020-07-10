# -*- coding:utf-8 -*-
# @Time: 2020/7/10 8:31 上午
# @Author: duiya duiyady@163.com


"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
"""

def uniquePaths(m, n):
    tmp = [[0 for _ in range(n)] for _ in range(m)]

    def fun(i, j, count):
        if i == m-1 and j == n-1:
            return count + 1
        else:
            if tmp[i][j] != 0:
                return count + tmp[i][j] - 1
            else:
                t_count = count
                if j+1 < n:
                    t_count = fun(i, j+1, t_count)
                if i+1 < m:
                    t_count = fun(i+1, j, t_count)
                tmp[i][j] = t_count - count + 1
                return t_count
    return fun(0, 0, 0)


if __name__ == '__main__':
    print(uniquePaths(3, 2))


