# -*- coding:utf-8 -*-
# @Time: 2019-09-15 23:09
# @Author: duiya duiyady@163.com


"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
"""

def findMedianSortedArrays(nums1, nums2):
    nums1_len, nums2_len = len(nums1), len(nums2)
    if nums1_len > nums2_len:
        nums1, nums2, nums1_len, nums2_len = nums2, nums1, nums2_len, nums1_len
    if nums2_len == 0:
        raise ValueError

    start, end, half_len = 0, nums1_len, (nums1_len + nums2_len + 1) // 2
    while start <= end:
        index_nums1 = (start + end) // 2
        index_nums2 = half_len - index_nums1
        if index_nums1 < nums1_len and nums2[index_nums2 - 1] > nums1[index_nums1]:
            # i is too small, must increase it
            start = index_nums1 + 1
        elif index_nums1 > 0 and nums1[index_nums1 - 1] > nums2[index_nums2]:
            # i is too big, must decrease it
            end = index_nums1 - 1
        else:
            # i is perfect
            if index_nums1 == 0:
                max_of_left = nums2[index_nums2 - 1]
            elif index_nums2 == 0:
                max_of_left = nums1[index_nums1 - 1]
            else:
                max_of_left = max(nums1[index_nums1 - 1], nums2[index_nums2 - 1])

            if (nums1_len + nums2_len) % 2 == 1:
                return max_of_left

            if index_nums1 == nums1_len:
                min_of_right = nums2[index_nums2]
            elif index_nums2 == nums2_len:
                min_of_right = nums1[index_nums1]
            else:
                min_of_right = min(nums1[index_nums1], nums2[index_nums2])

            return (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':
    print(findMedianSortedArrays([1, 2, 3], [2, 4]))
