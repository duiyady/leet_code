"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
输入: [ 1->4->5,
        1->3->4,
        2->6 ]
输出: 1->1->2->3->4->4->5->6
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists):
    tmps = lists
    min_index = 0
    now = None
    count_none = 0
    for i in range(len(lists)):
        if lists[i] is None:
            count_none += 1
            continue
        if now is None or lists[i].val < now.val:
            min_index = i
            now = tmps[i]
    result = now
    if count_none == len(lists):
        return None
    tmps[min_index] = tmps[min_index].next
    while len(tmps) != 0:
        remove_list = []
        count_none = 0
        tmp_now = None
        min_index = -1
        for i in range(len(tmps)):
            if tmps[i] is None:
                count_none += 1
                remove_list.append(i)
                continue
            if tmp_now is None or tmps[i].val < tmp_now.val:
                min_index = i
                tmp_now = tmps[i]
        if min_index != -1:
            now.next = tmp_now
            tmps[min_index] = tmps[min_index].next
            now = now.next
        for i in remove_list[::-1]:
            del tmps[i]
    return result


def mergeKLists2(lists):
    def mergeTwoLists(l1, l2):
        tmp1 = l1
        tmp2 = l2
        if l1 == None or l1 == []:
            return l2
        if l2 == None or l2 == []:
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

    if len(lists) == 0:
        return None
    elif len(lists) == 1:
        return lists[0]
    else:
        result = []
        for lis in lists:
            result = mergeTwoLists(result, lis)
        return result

if __name__ == '__main__':
    head1, tmp1, tmp2 = ListNode(1), ListNode(4), ListNode(5)
    head1.next = tmp1
    tmp1.next = tmp2
    head2, tmp1, tmp2 = ListNode(1), ListNode(3), ListNode(4)
    head2.next = tmp1
    tmp1.next = tmp2
    head3, tmp1 = ListNode(2), ListNode(6)
    head3.next = tmp1
    head = mergeKLists2([head1, head2, head3])
    while head is not None:
        print(head.val)
        head = head.next
