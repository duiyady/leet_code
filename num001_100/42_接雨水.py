# -*- coding:utf-8 -*-
# @Time: 2020/6/28 16:12
# @Author: duiya duiyady@163.com

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""

"""
如果经历了下和上，那么就算一次
每次经历下的时候都看一下是否要计算
"""

def trap(height):
    len_height = len(height)
    height.append(0)
    count = 0
    last_maxindex = -1
    while last_maxindex != len_height-1:
        max_index = last_maxindex + 1
        for i in range(max_index, len_height):
            if height[i] >= height[max_index]:
                max_index = i
        now_height = min(height[last_maxindex], height[max_index])
        for i in range(last_maxindex+1, max_index):
            if height[i] > now_height:
                now_height = height[i]
            elif height[i] < now_height:
                count += (now_height-height[i])
        last_maxindex = max_index
    return count

if __name__ == '__main__':
    print(trap([4,3,2]))




