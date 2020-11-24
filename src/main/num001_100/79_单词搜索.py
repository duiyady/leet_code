# -*- coding:utf-8 -*-
# @Time: 2020/7/20 21:16
# @Author: duiya duiyady@163.com


"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
 

提示：
board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""


def exist(board, word):
    words_dict = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in words_dict.keys():
                words_dict[board[i][j]].append((i, j))
            else:
                words_dict[board[i][j]] = [(i, j), ]
    tmp = [[0]*len(board[0]) for _ in range(len(board))]
    def fun(index, last=None):
        if index == len(word):
            return True
        if word[index] in words_dict.keys():
            if index == 0:
                for va in words_dict[word[index]]:
                    tmp[va[0]][va[1]] = 1
                    tmp_res = fun(index+1, last=va)
                    if tmp_res:
                        return True
                    tmp[va[0]][va[1]] = 0
            else:
                for va in words_dict[word[index]]:
                    if tmp[va[0]][va[1]] == 0:
                        if (va[0] == last[0] and (va[1] == last[1]+1 or va[1] == last[1]-1)) or (va[1] == last[1] and (va[0] == last[0]+1 or va[0] == last[0]-1)):
                            tmp[va[0]][va[1]] = 1
                            tmp_res = fun(index+1, last=va)
                            if tmp_res:
                                return True
                            tmp[va[0]][va[1]] = 0
        return False
    return fun(0)


if __name__ == '__main__':
    print(exist(board=[['A', 'B', 'C', 'E'],
                       ['S', 'F', 'C', 'S'],
                       ['A', 'D', 'E', 'E']], word="SEE"))