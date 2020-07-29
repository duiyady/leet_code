# -*- coding:utf-8 -*-
# @Time: 2020/7/29 16:12
# @Author: duiya duiyady@163.com


"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderTraversal(root):
    if root is None:
        return []
    result = []
    stack = [[root, 0], ]
    while stack:
        tmp = stack[-1]
        now = len(stack)
        if tmp[1] == 0:
            tmp[1] = 1
            if tmp[0].left is not None:
                stack.insert(now, [tmp[0].left, 0])
            if tmp[0].right is not None:
                stack.insert(now-1, [tmp[0].right, 0])
        else:
            stack.pop()
            result.append(tmp[0].val)
    return result

if __name__ == '__main__':
    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root2.left = root3
    root1.right = root2
    print(inorderTraversal(root1))
