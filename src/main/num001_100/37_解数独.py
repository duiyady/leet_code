# -*- coding:utf-8 -*-
# @Time: 2020/6/26 10:24 上午
# @Author: duiya duiyady@163.com

def solveSudoku(board):
    import numpy as np
    need_put = {}
    board_tmp = np.zeros([9, 9], dtype=int)
    need_index = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                board_tmp[i][j] = int(board[i][j])
            else:
                dict_tmp = {}
                dict_tmp["i"] = i
                dict_tmp["j"] = j
                need_put[need_index] = dict_tmp
                need_index += 1
    # 找出需要填入值的每个位置可以填入哪些值
    for index in range(need_index):
        i, j = need_put[index]["i"], need_put[index]["j"]
        tmp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        i_s, j_s = (i//3)*3, (j//3)*3
        for x_i in range(9):
            if board_tmp[i][x_i] in tmp_list:
                tmp_list.remove(board_tmp[i][x_i])
            if board_tmp[x_i][j] in tmp_list:
                tmp_list.remove(board_tmp[x_i][j])
            if board_tmp[i_s+x_i//3][j_s+x_i%3] in tmp_list:
                tmp_list.remove(board_tmp[i_s+x_i//3][j_s+x_i%3])
        need_put[index]["option"] = tmp_list
    retrocactive(0, board_tmp, need_put)
    for index in range(need_index):
        i, j = need_put[index]["i"], need_put[index]["j"]
        board[i][j] = str(board_tmp[i][j])


def retrocactive(index, board_tmp, need_put):
    if index == len(need_put):  # 填入完成判断
        return True
    i, j, option = need_put[index]["i"], need_put[index]["j"], need_put[index]["option"]
    i_s, j_s = (i//3)*3, (j//3)*3
    for va in option:
        if va not in board_tmp[i, :] and va not in board_tmp[:, j] and va not in board_tmp[i_s: i_s+3, j_s: j_s+3]:
            board_tmp[i][j] = va
            flag = retrocactive(index+1, board_tmp, need_put)
            if flag is True:
                return True
            else:
                board_tmp[i][j] = 0
    return False





if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    solveSudoku(board)


