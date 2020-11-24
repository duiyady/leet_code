# -*- coding:utf-8 -*-
# @Time: 2020/9/28 9:20
# @Author: duiya duiyady@163.com


"""
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。
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