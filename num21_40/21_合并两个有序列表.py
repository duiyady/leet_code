"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    tmp1 = l1
    tmp2 = l2
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if tmp1.val < tmp2.val:
        now = tmp1
        tmp1 = tmp1.next
    else:
        now = tmp2
        tmp2 = tmp2.next
    result = now
    while tmp1 is not None and tmp2 is not None:
        if tmp1.val < tmp2.val:
            now.next = tmp1
            tmp1 = tmp1.next
        else:
            now.next = tmp2
            tmp2 = tmp2.next
        now = now.next
    if tmp1 is None:
        now.next = tmp2
    else:
        now.next = tmp1
    return result