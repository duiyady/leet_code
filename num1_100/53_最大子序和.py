# -*- coding:utf-8 -*-
# @Time: 2020/7/4 9:13
# @Author: duiya duiyady@163.com


"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""

def maxSubArray(nums):
    tmp_sum = [0]*len(nums)
    tmp_sum[0] = nums[0]
    now_max = nums[0]
    for i in range(1, len(nums)):
        if nums[i] >= 0:
            if tmp_sum[i-1] < 0:
                tmp_sum[i] = nums[i]
            else:
                tmp_sum[i] = nums[i] + tmp_sum[i-1]
        elif nums[i] < 0:
            if tmp_sum[i-1] <= 0:
                tmp_sum[i] = nums[i]
            else:
                tmp_sum[i] = nums[i] + tmp_sum[i - 1]
        now_max = max(now_max, tmp_sum[i])
    return now_max


if __name__ == '__main__':
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))