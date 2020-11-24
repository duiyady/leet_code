# -*- coding:utf-8 -*-
# @Time: 2020/7/30 15:16
# @Author: duiya duiyady@163.com


"""
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
示例 1:
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
输出: true
示例 2:
输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]
输出: false
示例 3:
输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]
输出: false
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    if (p is None and q is not None) or (q is None and p is not None):
        return False
    if p is None and q is None:
        return True
    if p.val != q.val:
        return False
    checks = [[p, q]]
    while checks:
        check = checks.pop()
        if check[0].left is not None and check[1].left is not None and check[0].left.val == check[1].left.val:
            checks.append([check[0].left, check[1].left])
        elif check[0].left is None and check[1].left is None:
            pass
        else:
            return False

        if check[0].right is not None and check[1].right is not None and check[0].right.val == check[1].right.val:
            checks.append([check[0].right, check[1].right])
        elif check[0].right is None and check[1].right is None:
            pass
        else:
            return False
    return True



