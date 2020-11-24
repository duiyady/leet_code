# -*- coding:utf-8 -*-
# @Time: 2020/7/22 20:21
# @Author: duiya duiyady@163.com

"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
示例 1:
输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:
输入: 1->1->1->2->3
输出: 2->3
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head):
    if head is None or head.next is None:
        return head
    result_head = None
    tmp_list = None
    tmp_now = head
    tmp_now_next = head.next
    flag = False
    while tmp_now_next is not None:
        if tmp_now.val == tmp_now_next.val:
            flag = True
        else:
            if flag is False:
                if result_head is None:
                    result_head = tmp_now
                    tmp_list = result_head
                else:
                    tmp_list.next = tmp_now
                    tmp_list = tmp_list.next
            flag = False
        tmp_now = tmp_now_next
        tmp_now_next = tmp_now_next.next

    if flag is False:
        if result_head is not None:
            tmp_list.next = tmp_now
            tmp_list = tmp_list.next
        else:
            result_head = tmp_now
            tmp_list = result_head
    if tmp_list is not None:
        tmp_list.next = None
    return result_head


if __name__ == '__main__':
    a1 = ListNode(1)
    a2 = ListNode(1)
    a3 = ListNode(2)
    a4 = ListNode(3)
    a5 = ListNode(4)
    a6 = ListNode(4)
    a7 = ListNode(5)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6
    a6.next = a7
    head = deleteDuplicates(a1)
    while head is not None:
        print(head.val)
        head = head.next


