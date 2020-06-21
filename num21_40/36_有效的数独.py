# -*- coding:utf-8 -*-
# @Time: 2020/6/21 10:52
# @Author: duiya duiyady@163.com

import numpy as np
from collections import Counter
"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
"""



def isValidSudoku(board):
    import numpy as np
    row_flag = np.zeros([9, 9])
    col_flag = np.zeros([9, 9])
    blo_flag = np.zeros([9, 9])
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                val = int(board[i][j])-1
                if row_flag[val][i] == 1 or col_flag[val][j] == 1 or blo_flag[val][(i//3)*3+j//3] == 1:
                    return False
                row_flag[val][i] = 1
                col_flag[val][j] = 1
                blo_flag[val][((i//3)*3+j//3)] = 1
    return True





if __name__ == '__main__':
    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(isValidSudoku(board))