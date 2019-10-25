# -*- encoding:utf-8 -*-
# @Time: 2019/10/25 13:55
# @Author duiya duiyady@163.com

"""
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""

def removeElement(nums, val):
    index_now = 0
    for num in nums:
        if num != val:
            nums[index_now] = num
            index_now += 1

    return index_now

if __name__ == '__main__':
    print(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))