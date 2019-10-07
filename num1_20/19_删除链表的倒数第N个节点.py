# -*- coding:utf-8 -*-
# @Time: 2019-10-07 17:25
# @Author: duiya duiyady@163.com


"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    tmp1 = ListNode(head.val)
    tmp1.next = head
    for i in range(n):
        tmp1 = tmp1.next
    tmp2 = ListNode(head.val)
    tmp2.next = head
    while tmp1.next != None:
        tmp1 = tmp1.next
        tmp2 = tmp2.next
    if tmp2.next is head:
        head = head.next
    else:
        tmp2.next = tmp2.next.next

    return head