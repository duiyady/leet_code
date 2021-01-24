package num1301_1400;


import javax.swing.*;
import java.util.HashSet;
import java.util.Set;

/**
 用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。
 网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。
 给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。 
 */

class Solution_1319 {
    public int makeConnected(int n, int[][] connections) {
        int length = connections.length;
        int[] root = new int[n];
        for(int i = 0; i < n; i++){
            root[i] = i;
        }
        for(int i = 0; i < length; i++){
            merge(root, connections[i][0], connections[i][1]);
        }
        int conn_num = 0;
        for(int i=0; i < root.length; i++){
            if (root[i] == i){
                conn_num += 1;
            }
        }
        if((n-1) > length){
            return -1;
        }
        return conn_num - 1;
    }

    public int find(int[] root, int a){
        int now_index = a;
        int now_root = root[now_index];
        while (now_index != now_root){
            now_index = now_root;
            now_root = root[now_index];
        }
        return now_root;
    }

    public void merge(int[] root, int a, int b){
        int a_root = find(root, a);
        int b_root = find(root, b);
        if(a_root != b_root) {
            root[b] = a_root;
            root[b_root] = a_root;
        }

    }

    public static void main(String[] args) {
        int[][] a = new int[3][2];
        a[0][0] = 0;
        a[0][1] = 1;
        a[1][0] = 0;
        a[1][1] = 2;
        a[2][0] = 1;
        a[2][1] = 2;
//        a[3][0] = 4;
//        a[3][1] = 5;

        Solution_1319 bawse = new Solution_1319();
        int res = bawse.makeConnected(4, a);
        System.out.println(res);
    }
}