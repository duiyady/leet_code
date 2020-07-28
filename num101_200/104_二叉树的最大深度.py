# -*- coding:utf-8 -*-
# @Time: 2020/7/28 14:02
# @Author: duiya duiyady@163.com


"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    def search(node):
        if node is None:
            return 0
        else:
            return max(search(node.left), search(node.right))+1
    return search(root)

def maxDepth2(root):
    count = 0
    tmp_0 = [root]
    tmp_1 = []
    flag = True
    while flag:
        flag = False
        if count % 2 == 0:
            while tmp_0:
                tmp = tmp_0.pop()
                if tmp is not None:
                    tmp_1.append(tmp.left)
                    tmp_1.append(tmp.right)
                    flag = True
        else:
            while tmp_1:
                tmp = tmp_1.pop()
                if tmp is not None:
                    tmp_0.append(tmp.left)
                    tmp_0.append(tmp.right)
                    flag = True
        count += 1
    return count - 1




