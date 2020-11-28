import javax.swing.*;
import java.util.ArrayList;
import java.util.List;

/**
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
例如，给定三角形：
[
[2],
[3,4],
[6,5,7],
[4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
 */

class Solution {
    public static int minimumTotal(List<List<Integer>> triangle) {
        int size = triangle.size();
        int[] result = new int[size];
        for(int i = 0; i < size; i++){
            result[i] = triangle.get(size-1).get(i);
        }

        for(int i = size-1; i > 0; i--){
            for(int j = 0; j < i; j++){
                result[j] = triangle.get(i-1).get(j) + Math.min(result[j], result[j+1]);
            }
        }
        return result[0];
    }

    public static void main(String[] args) {
        List<List<Integer>> tmp = new ArrayList<>();
        List<Integer> a = new ArrayList<>();
        a.add(2);
        List<Integer> b = new ArrayList<>();
        b.add(3);
        b.add(4);
        List<Integer> c = new ArrayList<>();
        c.add(5);
        c.add(6);
        c.add(7);
        List<Integer> d = new ArrayList<>();
        d.add(4);
        d.add(1);
        d.add(8);
        d.add(3);
        tmp.add(a);
        tmp.add(b);
        tmp.add(c);
        tmp.add(d);
        System.out.println(minimumTotal(tmp));



    }
}
