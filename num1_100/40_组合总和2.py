# -*- coding:utf-8 -*-
# @Time: 2020/6/27 11:14 上午
# @Author: duiya duiyady@163.com


"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
说明：
所有数字（包括目标数）都是正整数。解集不能包含重复的组合。 
"""


def combinationSum2(candidates, target):
    can_len = len(candidates)
    for i in range(0, can_len - 1):
        minpts = i
        for j in range(i, can_len):
            if candidates[j] < candidates[minpts]:
                minpts = j
        tmp = candidates[i]
        candidates[i] = candidates[minpts]
        candidates[minpts] = tmp
    print(candidates)
    result = []  # 记录最后的
    stack = [candidates[0]]  # 当前栈有哪些值
    stack_index = [0]  # 当前栈值的坐标
    pop = None  # 是否弹出来来
    while len(stack) > 0:
        # 如果上一次弹出
        if pop is not None:
            # 栈的最后一个为选择的最后一个继续弹出
            if stack_index[-1] >= can_len - 1:
                pop = stack.pop()
                stack_index.pop()
            else:  # 跳到下一个
                next_index = stack_index[-1]+1
                while next_index < can_len and candidates[next_index] == stack[-1]:
                    next_index += 1
                if next_index < can_len:
                    stack_index[-1] = next_index
                    stack[-1] = candidates[stack_index[-1]]
                    pop = None
                else:
                    pop = stack.pop()
                    stack_index.pop()
        else:
            count = sum(stack)
            if count == target:
                result.append(stack.copy())
                if stack_index[-1] == can_len - 1:
                    pop = stack.pop()
                    stack_index.pop()
                else:
                    next_index = stack_index[-1] + 1
                    while next_index < can_len and candidates[next_index] == stack[-1]:
                        next_index += 1
                    if next_index < can_len:
                        stack_index[-1] = next_index
                        stack[-1] = candidates[stack_index[-1]]
                        pop = None
                    else:
                        pop = stack.pop()
                        stack_index.pop()
            if count < target:
                if stack_index[-1] == can_len-1:
                    pop = stack.pop()
                    stack_index.pop()
                else:
                    stack_index.append(stack_index[-1]+1)
                    stack.append(candidates[stack_index[-1]])
                    pop = None
            if count > target:
                pop = stack.pop()
                stack_index.pop()

    return result


if __name__ == '__main__':
    print(combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))