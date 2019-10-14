"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
给定 1->2->3->4, 你应该返回 2->1->4->3.
"""
# class ListNode:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    if head == None:
        return None
    tmp1 = head
    tmp2 = head.next
    if tmp1 is None or tmp2 is None:
        return tmp1
    result = tmp2
    last = None
    while tmp1 is not None and tmp2 is not None:
        tmp1.next = tmp2.next
        tmp2.next = tmp1
        if last is None:
            last = tmp1
        else:
            last.next = tmp2
            last = tmp1
        if tmp1.next is not None:
            tmp2 = tmp1.next.next
            tmp1 = tmp1.next
        else:
            tmp1 = None
            tmp2 = None
    return result


if __name__ == '__main__':
    head, node1, node2, node3, node4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    result = swapPairs(head)
    while result is not None:
        print(result.val)
        result = result.next