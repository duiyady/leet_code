# -*- coding:utf-8 -*-
# @Time: 2020/7/22 10:08
# @Author: duiya duiyady@163.com


"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
示例 1：
输入：[3,4,5,1,2]
输出：1
示例 2：
输入：[2,2,2,0,1]
输出：0
"""


def minArray(numbers):
    if len(numbers) == 0:
        return
    elif len(numbers) == 1:
        return numbers[0]
    start, end = 0, len(numbers) - 1
    while start < end:
        if numbers[start] < numbers[end]:
            return numbers[start]
        else:
            mid = (start + end) // 2
            if numbers[mid] < numbers[end]:
                end = mid
            elif numbers[mid] == numbers[end]:
                start += 1
                end -= 1
            else:
                start = mid + 1
    return numbers[end]

if __name__ == '__main__':
    print(minArray([2,2,2,0,1]))