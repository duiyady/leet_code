package num001_100;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

 示例：
 输入：3
 输出：
 [
   [1,null,3,2],
   [3,2,null,1],
   [3,1,null,null,2],
   [2,1,3],
   [1,null,2,null,3]
 ]
 解释：
 以上的输出对应以下 5 种不同结构的二叉搜索树：
 1         3     3      2      1
 \       /     /      / \      \
 3     2     1      1   3      2
 /     /       \                 \
 2     1         2                 3
 */


class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;
     TreeNode() {}
     TreeNode(int val) { this.val = val; }
     TreeNode(int val, TreeNode left, TreeNode right) {
         this.val = val;
         this.left = left;
         this.right = right;
      }
  }

class Solution_95 {
    public List<TreeNode> generateTrees(int n) {
        List<TreeNode> result = new ArrayList<>();
        Map<Integer, List<TreeNode>> map = new HashMap<>();
        TreeNode tmp = new TreeNode(1);
        ArrayList<TreeNode> tmpList = new ArrayList<>();
        tmpList.add(tmp);
        map.put(0, new ArrayList<>());
        map.put(1, tmpList);
        for (int i = 2; i < n; i++) {
            tmpList = new ArrayList<>();
            for(int head = 1; head <= i; head++){

                int right_start = 1;
                int right_end = head-1;
                int left_start = head+1;
                int left_end = i;
                //只有左边
                if(right_end < right_start && left_end >= left_start){
                    List<TreeNode> per = map.get(left_end-left_start+1);
                    for(int num=0; num < per.size(); num++){
                        tmp = new TreeNode(head);
                        tmp.right = null;
                        tmp.left = this.copyNode(per.get(num));
                        tmpList.add(tmp, 0);
                    }
                }
                //只有右边
                else if(right_end >= right_start && left_end < left_start){

                }
                // 两边
                else if(right_end >= right_start && left_end >= left_start){

                }
            }
            map.put(i, tmpList);
        }
        return map.get(n);
    }

    public TreeNode copyNode(TreeNode node, int addValue){

    }

    public static void main(String[] args) {
        Solution_95 base = new Solution_95();
        base.generateTrees(3);
    }
}