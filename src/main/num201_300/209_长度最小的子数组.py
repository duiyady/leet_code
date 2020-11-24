# -*- coding:utf-8 -*-
# @Time: 2020/6/28 10:19
# @Author: duiya duiyady@163.com


"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。
示例: 
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
"""



def minSubArrayLen(s, nums):
    start = -1
    nums.append(0)
    now_len = len(nums)
    for i in range(0, len(nums) - 1):
        nums[i] = nums[i] + nums[i-1]
        if nums[i] - nums[start] >= s:
            for j in range(start, i):
                if nums[i] - nums[j] >= s:
                    if i-j < now_len:
                        now_len = i - j
                    start = j
                else:
                    break
            start += 1
    if now_len != len(nums):
        return now_len
    else:
        return 0

if __name__ == '__main__':
    print(minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]))