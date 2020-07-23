# -*- coding:utf-8 -*-
# @Time: 2020/7/23 8:31
# @Author: duiya duiyady@163.com


"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
"""


def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1_len = len(nums1)
    for i in reversed(range(m)):
        nums1[i + nums1_len - m] = nums1[i]
    nums1_index = 0
    nums2_index = 0
    for i in range(m+n):
        if nums1_index < m and nums2_index < n:
            if nums1[nums1_index + nums1_len - m] > nums2[nums2_index]:
                nums1[i] = nums2[nums2_index]
                nums2_index += 1
            else:
                nums1[i] = nums1[nums1_index + nums1_len - m]
                nums1_index += 1
        elif nums1_index < m:
            nums1[i] = nums1[nums1_index + nums1_len - m]
            nums1_index += 1
        else:
            nums1[i] = nums2[nums2_index]
            nums2_index += 1

    for i in range(m+n, nums1_len):
         nums1[i] = 0


if __name__ == '__main__':
    merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
