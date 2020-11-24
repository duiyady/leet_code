# -*- coding:utf-8 -*-
# @Time: 2020/7/31 9:50
# @Author: duiya duiyady@163.com


def findMagicIndex(nums):
    for i in range(len(nums)):
        if i == nums[i]:
            return i
    return -1