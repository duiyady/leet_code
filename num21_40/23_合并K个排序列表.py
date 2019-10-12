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
            now = lists[i]
    result = now
    if count_none == len(lists):
        return []
    tmps[min_index] = tmps[min_index].next
    while(count_none != len(lists)):
        count_none = 0
        tmp_now = None
        min_index = -1
        for i in range(len(lists)):
            if tmps[i] is None:
                count_none += 1
                continue
            if now is None or lists[i].val < now.val:
                min_index = i
                tmp_now = lists[i]
        if min_index != -1:
            now.next = tmp_now
            tmps[min_index] = tmps[min_index].next
            now = now.next
    return result




    return None
