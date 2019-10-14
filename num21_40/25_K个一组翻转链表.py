"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseKGroup(head, k):
    count = 0
    l_s, l_n, n_s, n_n = None, None, None, None
    now  = head
    result = None
    while now is not None:
        count += 1
        if count%k == 0:
            pass
        else:
            if 
