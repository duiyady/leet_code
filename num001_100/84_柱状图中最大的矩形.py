# -*- coding:utf-8 -*-
# @Time: 2020/7/25 17:24
# @Author: duiya duiyady@163.com


"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
输入: [2,1,5,6,2,3]
输出: 10
"""

def largestRectangleArea(heights):
    len_hei = len(heights)
    if len_hei == 0:
        return 0
    left = [0]*len_hei
    right = [len_hei-1]*len_hei
    stack_left = [0]
    stack_right = [len_hei-1]
    for i in range(1, len(heights)):
        while stack_left and heights[stack_left[-1]] >= heights[i]:
            stack_left.pop()
        if stack_left:
            left[i] = stack_left[-1]+1
        else:
            left[i] = 0
        stack_left.append(i)


        while stack_right and heights[stack_right[-1]] >= heights[-i-1]:
            stack_right.pop()
        if stack_right:
            right[-i-1] = stack_right[-1] - 1
        else:
            right[-i - 1] = len_hei - 1
        stack_right.append(len_hei-i-1)
    result = 0
    for i in range(len_hei):
        result = max(result, heights[i]*(right[i]-left[i] + 1))
    return result





if __name__ == '__main__':
    print(largestRectangleArea([2,9,9,0,4,5,0,1,6,9,5,8,8,1]))