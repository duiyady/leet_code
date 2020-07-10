# -*- coding:utf-8 -*-
# @Time: 2020/7/2 21:14
# @Author: duiya duiyady@163.com


def solveNQueens(n):
    results_index = []
    step = 0
    indexs = [-1]*n
    while step != -1:
        if step == n:
            results_index.append(indexs.copy())
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
                    if indexs[i] == indexs[step] or indexs[i]-i == indexs[step]-step or indexs[i]+i == indexs[step]+step:
                        flag = False
                        break
                if flag:
                    step += 1

    results = []
    for val in results_index:
        a = ["."]*n
        tmp = []
        for i in range(n):
            tmp.append(a.copy())
        for i in range(n):
            tmp[i][val[i]] = "Q"
            tmp[i] = "".join(tmp[i])
        results.append(tmp)
    return results


if __name__ == '__main__':
    print(solveNQueens(4))


