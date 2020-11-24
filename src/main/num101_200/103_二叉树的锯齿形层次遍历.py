# -*- coding:utf-8 -*-
# @Time: 2020/9/3 9:18
# @Author: duiya duiyady@163.com


"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：
[
  [3],
  [20,9],
  [15,7]
]
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def zigzagLevelOrder(root):
    if root is None:
        return []
    result = []
    need_cha = [root]

    while need_cha:
        result.append([node.val for node in need_cha])
        tmp = []
        for node in reversed(need_cha):
            if len(result)%2 == 0:
                if node.left is not None:
                    tmp.append(node.left)
                if node.right is not None:
                    tmp.append(node.right)
            else:
                if node.right is not None:
                    tmp.append(node.right)
                if node.left is not None:
                    tmp.append(node.left)
        need_cha = tmp
    return result

