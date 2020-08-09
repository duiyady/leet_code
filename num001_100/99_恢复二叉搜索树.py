# -*- coding:utf-8 -*-
# @Time: 2020/8/8 15:06
# @Author: duiya duiyady@163.com


"""
二叉搜索树中的两个节点被错误地交换。
请在不改变其结构的情况下，恢复这棵树。

示例 1:
输入: [1,3,null,null,2]
   1
  /
 3
  \
   2
输出: [3,1,null,null,2]
   3
  /
 1
  \
   2

示例 2:
输入: [3,1,4,null,null,2]
  3
 / \
1   4
   /
  2
输出: [2,1,4,null,null,3]
  2
 / \
1   4
   /
  3
进阶:
使用 O(n) 空间复杂度的解法很容易实现。
你能想出一个只使用常数空间的解决方案吗？
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root):
    """
    Do not return anything, modify root in-place instead.
    """
    tmp = []

    def zxbl(root):
        if root:
            zxbl(root.left)
            tmp.append(root)
            zxbl(root.right)
    zxbl(root)
    change1 = None
    change2 = tmp[-1]
    for i in range(1, len(tmp)):
        if tmp[i].val < tmp[i-1].val:
            if change1 is None:
                change1 = tmp[i-1]
                change2 = tmp[i]
            else:
                change2 = tmp[i]

    change1.val, change2.val = change2.val, change1.val







if __name__ == '__main__':
    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root4 = TreeNode(4)
    root5 = TreeNode(5)
    root6 = TreeNode(6)
    root7 = TreeNode(7)
    root8 = TreeNode(8)
    root1.left = root2
    root1.right = root3
    root2.left = root4
    root2.right = root5
    root3.left = root6
    root3.right = root7
    recoverTree(root1)
