# -*- coding:utf-8 -*-
# @Time: 2020-03-21 11:00
# @Author: duiya duiyady@163.com

"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
"""

def searchRange(nums, target):
    start, end, mid = 0, len(nums)-1, 0
    flag = False
    while start <= end:
        mid = (start + end)//2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            flag = True
            break
    if flag is False:
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
        return [-1, -1]

    start1, end1, mid1 = start, mid, 0
    start2, end2, mid2 = mid, end, 0
    while start1 <= end1:
        mid1 = (start1 + end1)//2
        if nums[mid1] < target:
            start1 = mid1 + 1
        elif nums[mid1] > target:
            end1 = mid1 - 1
        else:
            end1 -= 1
    while start2 <= end2:
        mid2 = (start2 + end2) // 2
        if nums[mid2] < target:
            start2 = mid2 + 1
        elif nums[mid2] > target:
            end2 = mid2 - 1
        else:
            start2 += 1
    return [start1, end2]


if __name__ == '__main__':
    print(searchRange([1,4], 4))