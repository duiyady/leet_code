# -*- coding:utf-8 -*-
# @Time: 2020/7/11 8:10 上午
# @Author: duiya duiyady@163.com


"""
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
示例:
输入: [5,2,6,1]
输出: [2,1,1,0]
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.
"""

# 时间复杂度太高
def countSmaller(nums):
    if len(nums) == 0:
        return
    tmp_nums = sorted(set(nums))
    tmp_count = [0] * len(tmp_nums)
    result = [0]*len(nums)
    index = {tmp_nums[i]: i for i in range(len(tmp_nums))}
    for i in reversed(range(len(nums))):
        result[i] = sum(tmp_count[: index[nums[i]]])
        tmp_count[index[nums[i]]] += 1
    return result


if __name__ == '__main__':
    print(countSmaller([5,2,6,1, 0]))



