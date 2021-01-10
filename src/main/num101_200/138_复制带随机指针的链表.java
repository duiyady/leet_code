import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
 要求返回这个链表的 深拷贝。 
 我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
 val：一个表示 Node.val 的整数。
 random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
 */


class Node138 {
    int val;
    Node138 next;
    Node138 random;

    public Node138(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}


class Solution138 {
    public Node138 copyRandomList(Node138 head) {
        if(head == null){
            return null;
        }
        Map<Object, Integer> map = new HashMap<>();
        int now = 0;
        List<Node138> list = new ArrayList<>();
        Node138 ori = head;
        Node138 copy_head = new Node138(ori.val);
        Node138 copy_pre = copy_head;
        map.put(ori, now);
        now++;
        list.add(copy_pre);
        while (ori.next != null){
            ori = ori.next;
            Node138 copy_next = new Node138(ori.val);
            map.put(ori, now);
            list.add(copy_next);
            now++;
            copy_pre.next = copy_next;
            copy_pre = copy_pre.next;
        }
        ori = head;
        now = 0;
        while (ori != null){
            if(ori.random != null){
                list.get(now).random = list.get(map.get(ori.random));
            }
            now += 1;
            ori = ori.next;
        }
        return copy_head;
    }
}