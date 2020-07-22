# -*- coding:utf-8 -*-
# @Time: 2020/7/22 21:10
# @Author: duiya duiyady@163.com


"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
示例 1:
输入: 1->1->2
输出: 1->2
示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):
    if head is None or head.next is None:
        return head
    result_head = head
    tmp = result_head
    tmp_now = head.next
    while tmp_now is not None:
        if tmp_now.val != tmp.val:
            tmp.next = tmp_now
            tmp = tmp.next
        tmp_now = tmp_now.next
    tmp.next = None
    return result_head