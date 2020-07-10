# -*- coding:utf-8 -*-
# @Time: 2020/7/10 8:47 上午
# @Author: duiya duiyady@163.com


"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""

def maxProfit(prices):
    result = [[0 for _ in range(3)] for _ in range(len(prices))]
    #  0当前位置买入的最大收益，1刚卖，2不买
    result[0][0] = -prices[0]
    for i in range(1, len(prices)):
        result[i][0] = max(result[i - 1][0], result[i - 1][2] - prices[i])
        result[i][1] = result[i - 1][0] + prices[i]
        result[i][2] = max(result[i - 1][1], result[i - 1][2])
    return max(result[len(prices)-1][1], result[len(prices)-1][2])

if __name__ == '__main__':
    print(maxProfit([1, 2, 3, 0, 2]))



