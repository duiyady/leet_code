# -*- coding:utf-8 -*-
# @Time: 2020/7/29 15:50
# @Author: duiya duiyady@163.com


"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseBetween(head, m, n):
    if m == 1:
        start = head
        last = head
        while n > m:
            now = start.next
            start.next = now.next
            now.next = last
            last = now
            n -= 1
        return last
    else:
        flag = head
        num = n-m
        while m > 2:
            flag = flag.next
            m -= 1
        start = flag.next
        last = flag.next
        while num > 0:
            now = start.next
            start.next = now.next
            now.next = last
            last = now
            num -= 1
        flag.next = last
        return head


