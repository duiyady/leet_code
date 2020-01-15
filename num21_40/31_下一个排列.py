# -*- coding:utf-8 -*-
# @Time: 2020/1/15
# @Author: duiya duiyady@163.com

"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


def nextPermutation(nums):
    n_nums = len(nums)
    posi = n_nums
    while posi > 0:
        for i in reversed(range(posi-1)):
            if nums[i] < nums[i+1]:
                for k in range(i+1, posi-1):
                    if nums[k+1] < nums[i] or k+1 == posi:
                        tmp = nums[k]
                        nums[k] = nums[i]
                        nums[i] = tmp
                        break
                j = i+1
                k = posi-1
                while j < k:
                    tmp = nums[j]
                    nums[j] = nums[k]
                    nums[k] = tmp
                    j += 1
                    k -= 1
                posi = i
                break
        posi = 0

if __name__ == '__main__':
    x = [1,2,3]
    nextPermutation(x)
    print(x)
                
