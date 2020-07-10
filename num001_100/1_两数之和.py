# -*- coding:utf-8 -*-
# @Time: 2019-09-15 23:00
# @Author: duiya duiyady@163.com


"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


def twoSum(nums, target):
    result = {}

    for index, num in enumerate(nums):
        tmp = target - num
        if tmp in result:
            return [result[tmp], index]
        result[num] = index
    return None


if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))