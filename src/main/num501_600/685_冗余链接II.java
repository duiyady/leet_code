package num501_600;

import java.util.*;

/**
 在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。
 输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
 结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。
 返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

 示例 1:
 输入: [[1,2], [1,3], [2,3]]
 输出: [2,3]
 解释: 给定的有向图如下:
 1
 / \
 v   v
 2-->3

 示例 2:
 输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
 输出: [4,1]
 解释: 给定的有向图如下:
 5 <- 1 -> 2
 ^    |
 |    v
 4 <- 3
 */

class Solution_685 {
    public int[] findRedundantDirectedConnection(int[][] edges) {
        Map<Integer, List<Integer>> map = new HashMap<>();

        int[] root = new int[edges.length+1];
        for(int i = 1; i < root.length; i++){
            root[i] = i;
        }

        boolean check_all = true;
        int[][] need_check = new int[2][2];

        for(int i = 0; i < edges.length; i++){
            if(!map.containsKey(edges[i][0])){
                map.put(edges[i][0], new ArrayList<>());
            }
            map.get(edges[i][0]).add(edges[i][1]);
            if(root[edges[i][1]] != edges[i][1]){
                check_all = false;
                need_check[0][0] = root[edges[i][1]];
                need_check[0][1] = edges[i][1];
                need_check[1][0] = edges[i][0];
                need_check[1][1] = edges[i][1];
            }else {
                root[edges[i][1]] = edges[i][0];
            }
        }

        if(check_all){
            for(int index = edges.length-1; index >= 0; index--){
                int[] tmp_root = new int[root.length];
                int base_root = edges[index][1];
                int father = edges[index][0];
                for(int i = 0; i < tmp_root.length; i++) {
                    tmp_root[i] = root[i];
                }
                tmp_root[base_root] = base_root;

                if(check(map, tmp_root, base_root, father, base_root)){
                    return edges[index];
                }
            }
        }else {
            for(int index = 1; index >= 0; index--){
                int[] tmp_root = new int[root.length];
                int son = need_check[index][1];
                int father = need_check[index][0];
                for(int i = 0; i < tmp_root.length; i++){
                    tmp_root[i] = root[i];
                }
                tmp_root[son] = need_check[1-index][0];
                int now_index = son;
                int now_root = tmp_root[now_index];

                while (now_root != now_index){
                    now_index = now_root;
                    now_root = tmp_root[now_index];
                    if(now_index == son){
                        return need_check[1-index];
                    }
                }

                if(check(map, tmp_root, son, father, now_root)) {
                    return need_check[index];
                }
            }
        }
        return null;
    }

    public boolean check(Map<Integer, List<Integer>> map, int[] root, int son, int father, int base_root){
        map.get(father).remove((Object)son);
        List<Integer> stack = new LinkedList<>();
        stack.add(base_root);
        int count = 0;
        while (stack.size() > 0){
            int now_check = stack.get(0);
            List<Integer> nei = map.get(now_check);
            if(nei != null) {
                for (int i = 0; i < nei.size(); i++) {
                    if (root[nei.get(i)] != now_check) {
                        break;
                    }
                    stack.add(nei.get(i));
                    root[nei.get(i)] = base_root;
                }
            }
            stack.remove(0);
            count += 1;
        }
        map.get(father).add(son);
        if(count == root.length-1){
            return true;
        }else {
            return false;
        }

    }


    public static void main(String[] args) {
        int[][] a = new int[3][2];
        a[0][0] = 1;
        a[0][1] = 2;
        a[1][0] = 1;
        a[1][1] = 3;
        a[2][0] = 2;
        a[2][1] = 3;
        num501_600.Solution_685 bawse = new num501_600.Solution_685();
        int[] res = bawse.findRedundantDirectedConnection(a);
        System.out.println(res[0] + " " + res[1]);

    }
}