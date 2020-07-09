# -*- coding:utf-8 -*-
# @Time: 2020/7/9 8:43
# @Author: duiya duiyady@163.com


"""
给定一个链表，旋转链表，将链表每个节点向右移动k个位置，其中k是非负数。
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def rotateRight(head, k):
    if head is None:
        return
    if head.next is not None:
        t_head = head.next
    else:
        return head
    count = 2
    while t_head.next is not None:
        t_head = t_head.next
        count += 1
    t_head.next = head
    k = k % count
    t_c = count - k
    while t_c > 0:
        t_head = t_head.next
        t_c -= 1
    tmp_root = t_head.next
    t_head.next = None
    return tmp_root

if __name__ == '__main__':
    root = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(4)
    n4 = ListNode(5)
    n3.next = n4
    n2.next = n3
    n1.next = n2
    root.next = n1
    tmp = rotateRight(root, 1)
    while tmp is not None:
        print(tmp.val)
        tmp = tmp.next
