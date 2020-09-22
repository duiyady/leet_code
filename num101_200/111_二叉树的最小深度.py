# -*- coding:utf-8 -*-
# @Time: 2020/9/22 9:13
# @Author: duiya duiyady@163.com


"""
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。

示例:
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minDepth(root):
    if root is None:
        return 0

    count = 1
    tmp = [root]
    while len(tmp) > 0:
        tmp2 = []
        for node in tmp:
            flag = False
            if node.left is not None:
                tmp2.append(node.left)
                flag = True
            if node.right is not None:
                tmp2.append(node.right)
                flag = True
            if flag is False:
                return count
        count += 1
        tmp = tmp2
