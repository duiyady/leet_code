# -*- coding:utf-8 -*-
# @Time: 2020/7/6 17:00
# @Author: duiya duiyady@163.com


"""
给出一个区间的集合，请合并所有重叠的区间。
示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
"""


def merge(intervals):
    for i in range(len(intervals) - 1):
        min = i
        for j in range(i + 1, len(intervals)):
            if intervals[j][0] < intervals[min][0]:
                min = j
        tmp = intervals[min]
        intervals[min] = intervals[i]
        intervals[i] = tmp
    i = 0
    while i < len(intervals) - 1:
        if intervals[i + 1][0] <= intervals[i][1]:
            intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
            intervals.pop(i + 1)
        else:
            i += 1
    return intervals


if __name__ == '__main__':
    print(merge([[1,3],[2,6],[8,10],[15,18]]))