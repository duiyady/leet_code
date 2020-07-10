# -*- coding:utf-8 -*-
# @Time: 2020/7/7 20:46
# @Author: duiya duiyady@163.com


"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(root, sum):
    if root is None:
        return False
    need_search = [root]
    while len(need_search) > 0:
        tmp = need_search.pop()
        if tmp.val == sum:
            if tmp.left is None and tmp.right is None:
                return True
        if tmp.left is not None:
            tmp.left.val += tmp.val
            need_search.append(tmp.left)
        if tmp.right is not None:
            tmp.right.val += tmp.val
            need_search.append(tmp.right)
    return False

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
    root = create_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    # root = create_tree([1, 2])
    # root = create_tree([[-2,None,-3]])
    # root = create_tree([1, 2, None, 3, None, 4, None, 5])

    print(hasPathSum(root, 22))






