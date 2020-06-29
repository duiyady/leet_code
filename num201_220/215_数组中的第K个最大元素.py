# -*- coding:utf-8 -*-
# @Time: 2020/6/29 8:07 上午
# @Author: duiya duiyady@163.com


"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
"""

def findKthLargest(nums, k):
    for i in range(0, k-1):
        min = i
        for j in range(i, k):
            if nums[j] < nums[min]:
                min = j
        tmp = nums[min]
        nums[min] = nums[i]
        nums[i] = tmp
    for i in range(k, len(nums)):
        if nums[i] > nums[0]:
            nums[0] = nums[i]
            for i in range(1, k):
                if nums[i] < nums[i-1]:
                    tmp = nums[i]
                    nums[i] = nums[i-1]
                    nums[i-1] = tmp
    return nums[0]


if __name__ == '__main__':
    print(findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
