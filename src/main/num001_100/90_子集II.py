# -*- coding:utf-8 -*-
# @Time: 2020/7/28 21:56
# @Author: duiya duiyady@163.com


"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

def subsetsWithDup(nums):
    result = [[], ]
    last_dict = {}
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
        tmp_result = []
        start = 0
        if nums[i] in last_dict.keys():
            start = last_dict[nums[i]]
        for index in range(start, len(result)):
            tt = result[index].copy()
            tt.append(nums[i])
            tmp_result.append(tt)
        last_dict[nums[i]] = len(result)
        result.extend(tmp_result)
    return result

if __name__ == '__main__':
    print(subsetsWithDup([1, 1, 2, 1]))


