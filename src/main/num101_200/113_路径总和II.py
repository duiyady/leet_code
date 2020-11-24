# -*- coding:utf-8 -*-
# @Time: 2020/9/24 16:16
# @Author: duiya duiyady@163.com

"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pathSum(root, sum):
    if root is None:
        return []
    stack = [root]
    state = [0]
    result = []

    while stack:
        print([tmp.val for tmp in stack])
        print(state)
        print("========================")


        if state[-1] == 0:
            if stack[-1].left is not None:
                stack.append(stack[-1].left)
                state[-1] = 1
                state.append(0)
            elif stack[-1].right is None:
                now = 0
                for tmp in stack:
                    now += tmp.val

                if now == sum:
                    result.append([tmp.val for tmp in stack])
                stack.pop()
                state.pop()
            else:
                state[-1] = 1
        elif state[-1] == 1:
            if stack[-1].right is not None:
                stack.append(stack[-1].right)
                state[-1] = 2
                state.append(0)
            else:
                state[-1] = 2
        else:
            stack.pop()
            state.pop()
    return result

def create_tree(nums):
    trees = []
    for i in range(len(nums)):
        if nums[i] != None:
            tree = TreeNode(nums[i])
            fa = (i-1)//2
            if fa >= 0:
                if i%2 == 0:
                    trees[fa].right = tree
                else:
                    trees[fa].left = tree
            trees.append(tree)
        else:
            trees.append(None)
    return trees[0]

if __name__ == '__main__':
    root = create_tree([1,-2,-3,1,3,-2,None,-1])
    print(pathSum(root, -1))
