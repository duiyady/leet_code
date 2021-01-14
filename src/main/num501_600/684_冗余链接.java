package num501_600;

import javax.swing.*;

/**
 在本问题中, 树指的是一个连通且无环的无向图。
 输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
 结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。
 返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

 示例 1：
 输入: [[1,2], [1,3], [2,3]]
 输出: [2,3]
 解释: 给定的无向图为:
 1
 / \
 2 - 3

 示例 2：
 输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
 输出: [1,4]
 解释: 给定的无向图为:
 5 - 1 - 2
 |   |
 4 - 3
 */

class Solution_684 {
    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        int[] root = new int[n+1];
        for(int i = 1; i < root.length; i++){
            root[i] = i;
        }

        for(int i = 0; i < edges.length; i++){
            if(!merge(root, edges[i][0], edges[i][1])){
                return edges[i];
            }
        }
        return null;
    }

    public int find(int[] root, int a){
        int now_root = root[a];
        int now_index = a;
        while (now_root != now_index){
            now_index = now_root;
            now_root = root[now_index];
        }
        return now_root;
    }

    public boolean merge(int[] root, int a, int b){
        int a_root = find(root, a);
        int b_root = find(root, b);
        if(a_root == b_root){
            return false;
        }else {
            root[b_root] = a_root;
            root[b] = a_root;
            return true;
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
        Solution_684 bawse = new Solution_684();
        int[] res = bawse.findRedundantConnection(a);
        System.out.println(res[0] + " " + res[1]);

    }
}