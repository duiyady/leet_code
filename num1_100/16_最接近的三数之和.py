# -*- coding:utf-8 -*-
# @Time: 2019-10-03 21:14
# @Author: duiya duiyady@163.com


"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2)
"""


def threeSumClosest(nums, target):
    now = None
    nums.sort()
    for k in range(len(nums) - 2):
        i, j = k+1, len(nums) - 1
        last = None
        while i < j:
            tmp = nums[k] + nums[i] + nums[j]
            if now is None:
                now = tmp
            if abs(tmp-target) < abs(now - target):
                now = tmp
            if last is not None and abs(tmp-target) > abs(last-target):
                break
            if (tmp-target) >= 0:
                j -= 1
            elif (tmp-target) < 0:
                i += 1

    return now


if __name__ == '__main__':
    print(threeSumClosest([-1, 2, 1 ,-4], 1))

