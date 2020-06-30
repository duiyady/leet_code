# -*- coding:utf-8 -*-
# @Time: 2020/6/30 8:48
# @Author: duiya duiyady@163.com

def jump(nums):
    count = len(nums)
    min_step = [count+1]*count
    for i in range(1, count+1):
        if nums[-i] != 0:
            min_step[-i] = 1
            if nums[-i] < i-1:
                min_pts = i-1
                if min_step[-min_pts] != 1:
                    for j in range(i-nums[-i], i-1):
                        if min_step[-j] < min_step[-min_pts]:
                            min_pts = j
                            if min_step[-min_pts] == 1:
                                break
                min_step[-i] += min_step[-min_pts]
    if min_step[0] < count:
        return min_step[0]
    else:
        return 0

def ju(nums):
    count = len(nums)
    min_step = [1] * count
    for i in range(1, count + 1):
        if nums[-i] != 0:
            if nums[-i] < i - 1:
                min_pts = i - 1
                if min_step[-min_pts] != 1:
                    for j in range(i - nums[-i], i - 1):
                        if min_step[-j] < min_step[-min_pts]:
                            min_pts = j
                            if min_step[-min_pts] == 1:
                                break
                min_step[-i] += min_step[-min_pts]
        else:
            min_step[-i] = count+1
    if min_step[0] < count:
        return min_step[0]
    else:
        return 0


if __name__ == '__main__':
    print(ju([0]))

