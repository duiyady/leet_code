# -*- coding:utf-8 -*-
# @Time: 2020/6/27 9:32 上午
# @Author: duiya duiyady@163.com


"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。解集不能包含重复的组合。
"""


def combinationSum(candidates, target):
    can_len = len(candidates)
    for i in range(0, can_len-1):
        minpts = i
        for j in range(i, can_len):
            if candidates[j] < candidates[minpts]:
                minpts = j
        tmp = candidates[i]
        candidates[i] = candidates[minpts]
        candidates[minpts] = tmp
    result = []  # 记录最后的
    stack = [candidates[0]]  # 当前栈有哪些值
    stack_index = [0]  # 当前栈值的坐标
    pop = False  # 是否弹出来来
    while len(stack) > 0:
        # 如果上一次弹出
        if pop:
            # 栈的最后一个为选择的最后一个继续弹出
            if stack_index[-1] >= can_len-1:
                stack.pop()
                stack_index.pop()
                pop = True
            else:  # 跳到下一个
                stack_index[-1] += 1
                stack[-1] = candidates[stack_index[-1]]
                pop = False
        else:
            count = sum(stack)
            if count == target:
                result.append(stack.copy())
                stack.pop()
                stack_index.pop()
                pop = True
            if count < target:
                stack_index.append(stack_index[-1])
                stack.append(candidates[stack_index[-1]])
                pop = False
            if count > target:
                stack.pop()
                stack_index.pop()
                pop = True

    return result



if __name__ == '__main__':
    print(combinationSum(candidates=[2,3, 5], target=8))