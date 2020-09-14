# -*- coding:utf-8 -*-
# @Time: 2020/9/14 8:38
# @Author: duiya duiyady@163.com


"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：
[
  [15,7],
  [9,20],
  [3]
]
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrderBottom(root):
    if root is None:
        return []
    tmp = [root]
    result = []
    while len(tmp) > 0:
        result.insert(0, [node.val for node in tmp])
        t_t = []
        for node in tmp:
            if node.left is not None:
                t_t.append(node.left)
            if node.right is not None:
                t_t.append(node.right)
        tmp = t_t
    return result
