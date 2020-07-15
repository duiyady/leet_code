# -*- coding:utf-8 -*-
# @Time: 2020/7/15 17:03
# @Author: duiya duiyady@163.com


"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
"""

def numTrees(n):
    result = [1] * (n+1)
    if n == 0:
        return 0
    result[1] = 1
    for i in range(2, n+1):
        count = 0
        for j in range(1, i//2 + 1):
            count = count + 2*(result[j-1]*result[i-j])
        if i%2 == 1:
            count += result[i//2]*result[i//2]
        result[i] = count
    return result[n]

if __name__ == '__main__':
    print(numTrees(100))