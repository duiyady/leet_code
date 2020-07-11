# -*- coding:utf-8 -*-
# @Time: 2020/7/11 8:10 上午
# @Author: duiya duiyady@163.com


"""
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
示例:
输入: [5,2,6,1]
输出: [2,1,1,0]
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.
"""

def countSmaller(nums):
    result = [0]*len(nums)
    tmp_nums = [0]*len(nums)  # 左边出现的数的排序
    nums_count = [0]*len(nums)  # 左边的数出现了几个
    tmp_count = 1  # 有几个不同的数
    tmp_nums[0] = nums[-1]
    nums_count[0] = 1
    for i in reversed(range(len(nums))):
        flag = False
        count = 0
        for j in range(tmp_count):
            if nums[i] == tmp_nums[j]:
                result[i] = count
                nums_count[j] += 1
                flag = True
                break
            elif nums[i] > tmp_nums[j]:
                result[i] = count + nums_count[j]
                tmp_nums.insert(j, nums[i])
                nums_count.insert(j, 1)
                tmp_count += 1
                flag = True
                break
            else:
                count += nums_count[j]
        if flag == False:
            result[i] = count
            tmp_nums.insert(tmp_count, nums[i])
            nums_count.insert(tmp_count, 1)
            tmp_count += 1
    print(result)
    return result


if __name__ == '__main__':
    print(countSmaller([5,2,6,1]))



