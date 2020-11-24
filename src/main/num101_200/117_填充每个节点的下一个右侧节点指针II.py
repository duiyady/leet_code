# -*- coding:utf-8 -*-
# @Time: 2020/11/7 17:39
# @Author: duiya duiyady@163.com


"""
给定一个二叉树
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。
进阶：
你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



def connect(root):
    if root is None:
        return

    now = [root]
    while now:
        tmp_now = []
        for i in range(len(now)):
            if now[i].left is not None:
                tmp_now.append(now[i].left)
            if now[i].right is not None:
                tmp_now.append(now[i].right)
            if i+1 < len(now):
                now[i].next = now[i+1]
        now = tmp_now
    return root