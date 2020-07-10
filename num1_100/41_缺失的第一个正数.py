# -*- coding:utf-8 -*-
# @Time: 2020/6/27 8:50 下午
# @Author: duiya duiyady@163.com

"""
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
示例 1:
输入: [1,2,0]
输出: 3
示例 2:
输入: [3,4,-1,1]
输出: 2
"""


def firstMissingPositive(nums):
    for i in range(len(nums)):
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != (i+1):
            tmp = nums[i]
            while tmp > 0 and tmp <= len(nums) and nums[tmp-1] != tmp:
                tmp_tmp = nums[tmp-1]
                nums[tmp-1] = tmp
                tmp = tmp_tmp
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1


if __name__ == '__main__':
    print(firstMissingPositive([3,4,-1,1]))
