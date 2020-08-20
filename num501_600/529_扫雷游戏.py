# -*- coding:utf-8 -*-
# @Time: 2020/8/20 20:03
# @Author: duiya duiyady@163.com


"""
让我们一起来玩扫雷游戏！
给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，
数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。
现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：\
如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板。

示例 1：
输入:
[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
Click : [3,0]
输出:
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
"""

def updateBoard(board, click):
    def change(click):
        board[click[0]][click[1]] = "B"
        for i in range(click[0] - 1, click[0] + 2):
            for j in range(click[1] - 1, click[1] + 2):
                if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and not (i == click[0] and j == click[1]):
                    if board[i][j] == "E":
                        count = 0
                        for m in range(i - 1, i + 2):
                            for n in range(j - 1, j + 2):
                                if m >= 0 and m < len(board) and n >= 0 and n < len(board[0]) and not (m == i and n == j):
                                    if board[m][n] == "M" or board[m][n] == "X":
                                        count += 1
                        if count == 0:
                            change([i, j])
                        else:
                            board[i][j] = count

    if board[click[0]][click[1]] == "M":
        board[click[0]][click[1]] = "X"
        return board
    else:
        count = 0
        for i in range(click[0] - 1, click[0] + 2):
            for j in range(click[1] - 1, click[1] + 2):
                if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and not(i == click[0] and j == click[1]):
                    if board[i][j] == "M" or board[i][j] == "X":
                        count += 1
        if count != 0:
            board[click[0]][click[1]] = count
            return board
        else:
            change(click)
            return board


if __name__ == '__main__':
    print(updateBoard(board=[["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click=[3, 0]))

