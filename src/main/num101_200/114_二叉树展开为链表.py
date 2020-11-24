# -*- coding:utf-8 -*-
# @Time: 2020/9/24 17:15
# @Author: duiya duiyady@163.com


"""
给定一个二叉树，原地将它展开为一个单链表。

例如，给定二叉树
    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    need_cha = []
    if root is None:
        return
    tmp_root = root
    while tmp_root.left is not None or len(need_cha) > 0 or tmp_root.right is not None:
        if tmp_root.left is not None:
            if tmp_root.right is not None:
                need_cha.insert(0, tmp_root.right)
            tmp_root.right = tmp_root.left
            tmp_root.left = None
            tmp_root = tmp_root.right

        elif tmp_root.right is not None:
            tmp_root = tmp_root.right
        else:
            next = need_cha.pop(0)
            tmp_root.right = next
            tmp_root = tmp_root.right


def create_tree(nums):
    trees = []
    for i in range(len(nums)):
        if nums[i] != None:
            tree = TreeNode(nums[i])
            fa = (i-1)//2
            if fa >= 0:
                if i%2 == 0:
                    trees[fa].right = tree
                else:
                    trees[fa].left = tree
            trees.append(tree)
        else:
            trees.append(None)
    return trees[0]

if __name__ == '__main__':
    root = create_tree([1,-2,-3,1,3,-2,None,-1])
    flatten(root)
    while root:
        print(root.val)
        root = root.right

