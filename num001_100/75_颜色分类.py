# -*- coding:utf-8 -*-
# @Time: 2020/7/18 10:09
# @Author: duiya duiyady@163.com


"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
注意:
不能使用代码库中的排序函数来解决这道题。
示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
"""


def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    start, end = 0, len(nums)-1
    while start < len(nums) and nums[start] == 0:
        start += 1
    while end >= 0 and nums[end] == 2:
        end -= 1
    if start == len(nums) or end == -1:
        return
    i = start
    while i <= end:
        if nums[i] == 0:
            nums[start] = 0
            start += 1
        elif nums[i] == 2:
            if nums[end] == 0:
                nums[start] = 0
                start += 1
            nums[end] = 2
            while end > i and nums[end] == 2:
                end -= 1
        if i >= start and i <= end:
            nums[i] = 1
        i += 1
    print(nums)

if __name__ == '__main__':
    sortColors([2, 0, 1])
    sortColors([2,0,2,1,1,2,2,0,1,1,1,0])
    sortColors([1, 0, 1])
    sortColors([2, 2, 0])