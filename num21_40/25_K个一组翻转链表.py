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
    if head is None or k == 1:
        return head
    count = 0
    l_s, l_e, n_s, n_e = None, None, None, None
    now = head
    result = None
    while now is not None:
        count += 1
        if count % k == 0:
            tmp = now.next
            now.next = n_s
            n_s = now
            if count // k == 1:
                result = n_s
            else:
                l_e.next = n_s
            l_s, l_e = n_s, n_e
            n_s, n_e = None, None
            now = tmp
        else:
            if count % k == 1:
                n_s = now
                n_e = now
                now = now.next
                n_e.next = None
            else:
                tmp = now.next
                now.next = n_s
                n_s = now
                now = tmp
    if n_s is not None:
        headt = None
        while n_s is not None:
            tmp = n_s.next
            if head is None:
                headt = n_s
                headt.next = None
            else:
                n_s.next = headt
                headt = n_s
            n_s = tmp
        n_s = headt
        if count // k == 0:
            result = n_s
        else:
            l_e.next = n_s


    return result


if __name__ == '__main__':
    head, node1, node2, node3, node4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    result = reverseKGroup(head, 3)
    while result is not None:
        print(result.val)
        result = result.next