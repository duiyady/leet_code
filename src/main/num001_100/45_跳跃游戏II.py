# -*- coding:utf-8 -*-
# @Time: 2020/6/30 8:48
# @Author: duiya duiyady@163.com


def jump(nums):
    count_step = 0
    i = 0
    while i < len(nums)-1:
        can_step = nums[i]
        if can_step == 0:
            return 0
        next_i = i+1
        if i + nums[i] >= len(nums)-1:
            next_i = len(nums)
        else:
            for j in range(i+2, i + nums[i]+1):
                if j+nums[j] > next_i+nums[next_i]:
                    next_i = j
        count_step += 1
        i = next_i
    return count_step



if __name__ == '__main__':
    print(jump([3,2,1,1]))

