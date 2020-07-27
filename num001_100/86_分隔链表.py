# -*- coding:utf-8 -*-
# @Time: 2020/7/26 11:18
# @Author: duiya duiyady@163.com


"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。
示例:
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def partition(head, x):
    if head is None or head.next is None:
        return head
    return_head = None
    # 找到第一个大于等于x的
    first_max = head
    first_max_last = None
    if head.val < x:
        return_head = head
        while first_max is not None and first_max.val < x:
            first_max = first_max.next
            if first_max_last is None:
                first_max_last = head
            else:
                first_max_last = first_max_last.next
    if first_max is not None:
        search = first_max.next
        search_last = first_max
        while search is not None:
            if search.val < x:
                if first_max_last is None:
                    search_last.next = search.next
                    return_head = search
                    first_max_last = return_head
                    first_max_last.next = first_max
                else:
                    search_last.next = search.next
                    first_max_last.next = search
                    search.next = first_max
                    first_max_last = first_max_last.next
                search = search_last.next
            else:
                search_last = search_last.next
                search = search.next
    if return_head is None:
        return_head = head
    return return_head



