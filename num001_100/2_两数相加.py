# -*- coding:utf-8 -*-
# @Time: 2019-09-15 23:02
# @Author: duiya duiyady@163.com


"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    n = l1.val + l2.val
    l3 = ListNode(n % 10)
    l3.next = ListNode(n // 10)
    p1 = l1.next
    p2 = l2.next
    p3 = l3
    while True:
        if p1 and p2:
            sum = p1.val + p2.val + p3.next.val
            p3.next.val = sum % 10
            p3.next.next = ListNode(sum // 10)
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
        elif p1 and not p2:
            sum = p1.val + p3.next.val
            p3.next.val = sum % 10
            p3.next.next = ListNode(sum // 10)
            p1 = p1.next
            p3 = p3.next
        elif not p1 and p2:
            sum = p2.val + p3.next.val
            p3.next.val = sum % 10
            p3.next.next = ListNode(sum // 10)
            p2 = p2.next
            p3 = p3.next
        else:
            if p3.next.val == 0:
                p3.next = None
            break
    return l3


if __name__ == '__main__':
    a1, b1, c1 = ListNode(2), ListNode(4), ListNode(3)
    a2, b2, c2 = ListNode(5), ListNode(6), ListNode(4)
    b1.next = c1
    a1.next = b1
    b2.next = c2
    a2.next = b2
    tmp = addTwoNumbers(a1, a2)
    while tmp:
        print(tmp.val)
        tmp = tmp.next