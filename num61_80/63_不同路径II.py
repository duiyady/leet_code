# -*- coding:utf-8 -*-
# @Time: 2020/7/6 11:11
# @Author: duiya duiyady@163.com


"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
"""

def uniquePathsWithObstacles(obstacleGrid):
    if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
        return 0
    def fun(i, j, count):
        t_count = count
        if i == len(obstacleGrid)-1 and j == len(obstacleGrid[0])-1:
            t_count += 1
        elif obstacleGrid[i][j] >= 3:
            t_count += (obstacleGrid[i][j]-3)
        else:
            if i+1 < len(obstacleGrid) and obstacleGrid[i+1][j] != 1:
                t_count = fun(i+1, j, t_count)
            if j+1 < len(obstacleGrid[0]) and obstacleGrid[i][j+1] != 1:
                t_count = fun(i, j+1, t_count)
            obstacleGrid[i][j] = t_count-count+3
        return t_count
    return fun(0, 0, 0)


if __name__ == '__main__':
    print(uniquePathsWithObstacles([[0, 0, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 0]]))
