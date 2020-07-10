# -*- coding:utf-8 -*-
# @Time: 2020/7/3 8:54
# @Author: duiya duiyady@163.com


"""
给定一个整数 n，返回 n 皇后不同的解决方案的数量。
"""


def totalNQueens(n):
    count = 0
    step = 0
    indexs = [-1] * n
    while step != -1:
        if step == n:
            count += 1
            step -= 2
            indexs[-1] = -1
        else:
            indexs[step] += 1
            if indexs[step] >= n:
                indexs[step] = -1
                step -= 1
            else:
                flag = True
                for i in range(step):
                    if indexs[i] == indexs[step] or indexs[i] - i == indexs[step] - step or indexs[i] + i == indexs[step] + step:
                        flag = False
                        break
                if flag:
                    step += 1
    return count

if __name__ == '__main__':
    print(totalNQueens(4))
