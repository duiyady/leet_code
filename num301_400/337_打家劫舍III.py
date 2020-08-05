# -*- coding:utf-8 -*-
# @Time: 2020/8/5 16:13
# @Author: duiya duiyady@163.com


"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:
输入: [3,2,3,null,3,null,1]
     3
    / \
   2   3
    \   \
     3   1
输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

示例 2:
输入: [3,4,5,1,3,null,1]
     3
    / \
   4   5
  / \   \
 1   3   1
输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
"""

class TreeNode:
    def __init__(self, x, name):
        self.val = x
        self.name = name
        self.left = None
        self.right = None

def rob(root):
    def tmp(node):
        if node is None:
            return 0, 0
        else:
            ls, ln = tmp(node.left)
            rs, rn = tmp(node.right)
            return node.val+ln+rn,  max(ls, ln)+max(rs, rn)

    return max(tmp(root))

if __name__ == '__main__':
    root = TreeNode(3, 0)
    node2 = TreeNode(2, 1)
    node3 = TreeNode(3, 2)
    node4 = TreeNode(3, 3)
    node5 = TreeNode(1, 4)
    root.left = node2
    root.right = node3
    node2.right = node4
    node3.right = node5
    print(rob(root))
