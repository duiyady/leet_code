# -*- coding:utf-8 -*-
# @Time: 2020/6/30 16:09
# @Author: duiya duiyady@163.com

"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。
示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


def permuteUnique(nums):
    for i in range(len(nums)-1):
        min_pts = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_pts]:
                min_pts = j
        nums[i], nums[min_pts] = nums[min_pts], nums[i]
    result = []
    tmp_choice = [0]*len(nums)
    tmp_nums = nums.copy()

    def recall(index):
        if index == len(nums):
            result.append(tmp_nums.copy())
            return
        last_use = None
        for i in range(len(nums)):
            if tmp_choice[i] == 0 and nums[i] != last_use:
                tmp_choice[i] = 1
                tmp_nums[index] = nums[i]
                recall(index+1)
                tmp_choice[i] = 0
                last_use = nums[i]
    recall(0)
    return result

if __name__ == '__main__':
    print(permuteUnique([-1,2,-1,2,1,-1,2,1]))