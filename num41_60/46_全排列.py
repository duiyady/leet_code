# -*- coding:utf-8 -*-
# @Time: 2020/6/30 14:55
# @Author: duiya duiyady@163.com

"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


def permute(nums):
    result = []
    tmp = [0]*len(nums)
    tmp_result = nums.copy()

    def recall(index):
        if index == len(nums):
            result.append(tmp_result.copy())
            return
        for i in range(len(nums)):
            if tmp[i] == 0:
                tmp_result[index] = nums[i]
                tmp[i] = 1
                recall(index+1)
                tmp[i] = 0

    recall(0)
    return result


if __name__ == '__main__':
    print(permute([1,2,3,4]))