# -*- coding:utf-8 -*-
# @Time: 2020/8/7 18:39
# @Author: duiya duiyady@163.com


"""
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
 
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
 

进阶：
你可以运用递归和迭代两种方法解决这个问题吗？
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root):
    if root is None:
        return True
    need_cha = [[root]]
    flag = True
    while len(need_cha) > 0 and flag:
        tmp = need_cha.pop()
        start, end = 0, len(tmp)-1
        while start <= end and flag:
            if tmp[start].left is not None and tmp[end].right is not None:
                if tmp[start].left.val != tmp[end].right.val:
                    flag = False
                    break
            if tmp[start].right is not None and tmp[end].left is not None:
                if tmp[start].right.val != tmp[end].left.val:
                    flag = False
                    break
            if (tmp[start].left is None and tmp[end].right is not None) or (tmp[start].left is not None and tmp[end].right is None) \
                    or (tmp[start].right is None and tmp[end].left is not None) or (tmp[start].right is not None and tmp[end].left is None):
                flag = False
                break
            start += 1
            end -= 1

        if flag:
            next = []
            for i in range(len(tmp)):
                if tmp[i].left is not None:
                    next.append(tmp[i].left)
                if tmp[i].right is not None:
                    next.append(tmp[i].right)
            if next:
                need_cha.append(next)
    return flag


if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)
    node7 = TreeNode(3)
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    print(isSymmetric(root))






