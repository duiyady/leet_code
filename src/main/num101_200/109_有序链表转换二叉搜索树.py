# -*- coding:utf-8 -*-
# @Time: 2020/9/19 21:44
# @Author: duiya duiyady@163.com


"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head):
    if head is None:
        return None
    pre, mid, next = get_mid(head)
    root = TreeNode(mid.val)
    root.left = sortedListToBST(pre)
    root.right = sortedListToBST(next)
    return root


def get_mid(head):
    fast = head
    slow = head
    slow_pre = None
    pre = None
    while fast is not None:
        fast = fast.next
        if fast is not None:
            fast = fast.next
            slow_pre = slow
            slow = slow.next
    if slow_pre is not None:
        slow_pre.next = None
        pre = head
    return pre, slow, slow.next


if __name__ == '__main__':
    A1 = ListNode(-10)
    A2 = ListNode(-3)
    A3 = ListNode(0)
    A4 = ListNode(5)
    A5 = ListNode(9)
    A1.next = A2
    A2.next = A3
    A3.next = A4
    A4.next = A5
    root = sortedListToBST(A1)



