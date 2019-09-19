# -*- coding:utf-8 -*-
# @Time: 2019-09-17 23:15
# @Author: duiya duiyady@163.com


"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""


def maxArea(height):
    max_vlaue = 0
    start = 0
    end = len(height) - 1
    while start < end:
        tmp = (end - start) * min(height[start], height[end])
        if tmp > max_vlaue:
            max_vlaue = tmp
        if height[start] > height[end]:
            end = end - 1
        else:
            start = start + 1
    return max_vlaue


if __name__ == '__main__':
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
