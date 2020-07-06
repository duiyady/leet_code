# -*- coding:utf-8 -*-
# @Time: 2020/7/6 17:09
# @Author: duiya duiyady@163.com


"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
"""


def insert(intervals, newInterval):
    index = -1
    for i in range(len(intervals)):
        if intervals[i][1] >= newInterval[0] and intervals[i][0] <= newInterval[0]:
            intervals[i][0], newInterval[0] = newInterval[0], intervals[i][0]
        if intervals[i][0] >= newInterval[0]:
            index = i
            break
    if index == -1:
        intervals.append(newInterval)
    else:
        intervals.insert(index, newInterval)
        while index < len(intervals) - 1:
            if intervals[index + 1][0] <= intervals[index][1]:
                intervals[index][1] = max(intervals[index][1], intervals[index + 1][1])
                intervals.pop(index + 1)
            else:
                index += 1
    return intervals



if __name__ == '__main__':
    print(insert(intervals=[[3,5]], newInterval=[1,3]))