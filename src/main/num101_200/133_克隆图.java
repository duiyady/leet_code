import java.util.ArrayList;
import java.util.List;

/**
 给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。
 图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

 class Node {
 public int val;
 public List<Node> neighbors;
 }
 */


// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}


class Solution {
    public Node cloneGraph(Node node) {
        if(node == null){
            return null;
        }
        List<Node> ori_list = new ArrayList<>();
        List<Node> copy_list = new ArrayList<>();

        int now_index = 0;
        ori_list.add(node);
        Node root = new Node(node.val);
        copy_list.add(root);
        while (now_index < ori_list.size()){
            Node tmp = ori_list.get(now_index);
            List<Node> neighbor = tmp.neighbors;
            Node copy = copy_list.get(now_index);
            List<Node> copy_neighbor = new ArrayList<>();
            for(Node val : neighbor){
                int index = ori_list.indexOf(val);
                // 存在
                if(index >= 0){
                    copy_neighbor.add(copy_list.get(index));
                }else {//不存在
                    Node w = new Node(val.val);
                    copy_neighbor.add(w);
                    ori_list.add(val);
                    copy_list.add(w);
                }
            }
            copy.neighbors = copy_neighbor;
            now_index++;
        }
        return copy_list.get(0);
    }
}