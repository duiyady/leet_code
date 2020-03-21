# -*- coding:utf-8 -*-
# @Time: 2020-01-30 17:31
# @Author: duiya duiyady@163.com


'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
'''


def search(nums, target):
    if not nums:
        return -1
    low, high = 0, len(nums)-1
    while low <= high:
        mid = (low+high)//2
        # 左边正常
        if nums[mid] >= nums[low]:
            if target >= nums[low] and target < nums[mid]:
                high = mid - 1
            elif target == nums[mid]:
                return mid
            else:
                low = mid + 1

        else:
            if target <= nums[high] and target > nums[mid]:
                low = mid + 1
            elif target == nums[mid]:
                return mid
            else:
                high = mid - 1
    return -1


if __name__ == '__main__':
    print(search([1,2,3,4,5,6,7], 3))