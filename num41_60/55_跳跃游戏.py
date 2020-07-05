# -*- coding:utf-8 -*-
# @Time: 2020/7/5 11:00 上午
# @Author: duiya duiyady@163.com


"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。
示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
"""


def canJump(nums):
    i = 0
    while i < len(nums) - 1:
        can_step = nums[i]
        if can_step == 0:
            return False
        next_i = i + 1
        if i + nums[i] >= len(nums) - 1:
            next_i = len(nums)
        else:
            for j in range(i + 2, i + nums[i] + 1):
                if j + nums[j] > next_i + nums[next_i]:
                    next_i = j
        i = next_i
    return True


if __name__ == '__main__':
    print(canJump([2,3,1,1,4]))