# -*- coding:utf-8 -*-
# @Time: 2019-10-07 16:38
# @Author: duiya duiyady@163.com

"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


def fourSum(nums, target):
    nums.sort()
    res, k = [], 0
    for k in range(len(nums)-3):
        if k > 0 and nums[k] == nums[k-1]:
            continue
        target2 = target-nums[k]
        for i in range(k+1, len(nums)-2):
            if i > k+1 and nums[i] == nums[i-1]:
                continue
            j, l = i+1, len(nums)-1
            while j < l:
                tmp = target2 - nums[i] - nums[j] - nums[l]
                if tmp < 0:
                    l -= 1
                    while j < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif tmp > 0:
                    j += 1
                    while j < l and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    res.append([nums[k], nums[i], nums[j], nums[l]])
                    j += 1
                    l -= 1
                    while j < l and nums[j] == nums[j-1]:
                        j += 1
                    while j < l and nums[l] == nums[l+1]:
                        l -= 1
    return res


if __name__ == '__main__':
    print(fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))