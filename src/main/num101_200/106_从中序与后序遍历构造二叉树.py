# -*- coding:utf-8 -*-
# @Time: 2020/9/12 19:45
# @Author: duiya duiyady@163.com


"""
根据一棵树的中序遍历与后序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。

例如，给出
中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(self, inorder, postorder):
    if len(inorder) == 0:
        return None
    index_dict = {}
    for i in range(len(inorder)):
        index_dict[inorder[i]] = i
    root = TreeNode(postorder[-1])
    stack = [root]
    for i in reversed(range(len(postorder)-1)):
        if index_dict[postorder[i]] > index_dict[stack[-1].val]:
            tmp = TreeNode(postorder[i])
            stack[-1].right = tmp
            stack.append(tmp)
        else:
            while stack and index_dict[stack[-1].val] > index_dict[postorder[i]]:
                top = stack.pop()
            tmp = TreeNode(postorder[i])
            top.left = tmp
            stack.append(tmp)
    return root


if __name__ == '__main__':
    pass