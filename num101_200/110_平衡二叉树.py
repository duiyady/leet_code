# -*- coding:utf-8 -*-
# @Time: 2020/8/17 8:48
# @Author: duiya duiyady@163.com


"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isBalanced(root):
    def height(root):
        if not root:
            return 0
        leftHeight = height(root.left)
        rightHeight = height(root.right)
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        else:
            return max(leftHeight, rightHeight) + 1

    return height(root) >= 0