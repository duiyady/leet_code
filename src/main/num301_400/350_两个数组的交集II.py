# -*- coding:utf-8 -*-
# @Time: 2020/7/13 9:47
# @Author: duiya duiyady@163.com


"""
给定两个数组，编写一个函数来计算它们的交集。
示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
"""

def intersect(nums1, nums2):
    if len(nums1) == 0 or len(nums2) == 0:
        return []
    result = []
    i, j = 0, 0
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return result


if __name__ == '__main__':
    print(intersect(nums1=[4,9,5], nums2=[9,4,9,8,4]))