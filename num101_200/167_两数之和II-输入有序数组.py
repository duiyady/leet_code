# -*- coding:utf-8 -*-
# @Time: 2020/7/20 10:57
# @Author: duiya duiyady@163.com

"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

示例:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""

def twoSum(numbers, target):
    if len(numbers) < 2:
        return
    index1, index2 = 0, len(numbers)-1
    while index1 < index2:
        tmp = numbers[index1] + numbers[index2]
        if tmp == target:
            return [index1+1, index2+1]
        elif tmp > target:
            index2 -= 1
        else:
            index1 += 1
    return


if __name__ == '__main__':
    print(twoSum(numbers=[2, 7, 11, 15], target=9))