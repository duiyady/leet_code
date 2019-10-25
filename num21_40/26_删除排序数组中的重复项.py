# -*- encoding:utf-8 -*-
# @Time: 2019/10/25 13:47
# @Author duiya duiyady@163.com

"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""
def removeDuplicates(nums):
    now_index = 0
    now_value = None

    for num in nums:
        if now_value is None or now_value != num:
            now_value = num
            nums[now_index] = now_value
            now_index += 1
    print(nums)
    return now_index

if __name__ == '__main__':
    print(removeDuplicates([1,1,2,3,4,5,5,6,6,7,7]))