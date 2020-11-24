# -*- coding:utf-8 -*-
# @Time: 2020/8/26 21:20
# @Author: duiya duiyady@163.com


"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
示例：
二叉树：[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(root):
    result = []
    if root is None:
        return result
    need_cha = [root]
    while need_cha:
        result.append([tt.val for tt in need_cha])
        tmp = []
        for node in need_cha:
            if node.left is not None:
                tmp.append(node.left)
            if node.right is not None:
                tmp.append(node.right)
        need_cha = tmp
    return result