# -*- coding:utf-8 -*-
# @Time: 2020/9/8 8:23
# @Author: duiya duiyady@163.com


"""
根据一棵树的前序遍历与中序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。
例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    stack = [root]

    inorderIndex = 0
    for i in range(1, len(preorder)):
        preorderVal = preorder[i]
        node = stack[-1]
        if node.val != inorder[inorderIndex]:
            node.left = TreeNode(preorderVal)
            stack.append(node.left)
        else:
            while stack and stack[-1].val == inorder[inorderIndex]:
                node = stack.pop()
                inorderIndex += 1
            node.right = TreeNode(preorderVal)
            stack.append(node.right)
    return root

