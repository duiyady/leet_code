# -*- coding:utf-8 -*-
# @Time: 2020/7/3 8:34
# @Author: duiya duiyady@163.com


"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    def fun(left, right):
        if left > right:
            return None
        mid = (right + left) // 2
        root = TreeNode(nums[mid])
        root.left = fun(left, mid - 1)
        root.right = fun(mid + 1, right)
        return root
    return fun(0, len(nums)-1)

if __name__ == '__main__':
    sortedArrayToBST([-10,-3,0,5,9])
