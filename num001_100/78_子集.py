# -*- coding:utf-8 -*-
# @Time: 2020/7/20 21:08
# @Author: duiya duiyady@163.com


"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

def subsets(nums):
    result = []
    tmp = []
    def fun(i):
        if i == len(nums):
            result.append(tmp.copy())
            return
        fun(i+1)

        tmp.append(nums[i])
        fun(i+1)
        tmp.pop()
    fun(0)
    return result


if __name__ == '__main__':
    print(subsets(nums=[1,2,3]))