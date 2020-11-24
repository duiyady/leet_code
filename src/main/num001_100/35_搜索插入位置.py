"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
示例 1:
输入: [1,3,5,6], 5
输出: 2
示例 2:
输入: [1,3,5,6], 2
输出: 1
"""


def searchInsert(nums, target):
    if len(nums) == 0:
        return 0
    start, end = 0, len(nums) - 1
    while start < end:
        mid = (start + end) // 2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        elif nums[mid] == target:
            start = end = mid
    if nums[start] >= target:
        return start
    elif nums[start] < target:
        return start + 1

if __name__ == '__main__':
    print(searchInsert([1, 3, 5, 6], 6))
    print(searchInsert([1, 3], 2))
    print(searchInsert([1], 0))
    print(searchInsert([1, 4, 6, 7, 8, 9], 6))
