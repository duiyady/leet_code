package num001_100;

import java.util.ArrayList;
import java.util.List;

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


class TreeNode_95 {
     int val;
     TreeNode_95 left;
     TreeNode_95 right;
     TreeNode_95() {}
     TreeNode_95(int val) { this.val = val; }
     TreeNode_95(int val, TreeNode_95 left, TreeNode_95 right) {
         this.val = val;
         this.left = left;
         this.right = right;
      }
  }

class Solution_95 {
    public List<TreeNode_95> generateTrees(int n) {
        return find(1, n);

    }
    public List<TreeNode_95> find(int start, int end){
        List<TreeNode_95> result = new ArrayList<>();
        if(start == end){
            TreeNode_95 tmp = new TreeNode_95(start);
            result.add(tmp);
            return result;
        }
        for(int headVal=start; headVal <= end; headVal++){
            if(headVal == start){
                List<TreeNode_95> rightListHead = find(headVal+1, end);
                for(TreeNode_95 val : rightListHead){
                    TreeNode_95 tmp = new TreeNode_95(headVal);
                    tmp.right = val;
                    result.add(tmp);
                }
            }else if(headVal == end){
                List<TreeNode_95> leftListHead = find(start, headVal-1);
                for(TreeNode_95 val : leftListHead){
                    TreeNode_95 tmp = new TreeNode_95(headVal);
                    tmp.left = val;
                    result.add(tmp);
                }
            }else {
                List<TreeNode_95> leftListHead = find(start, headVal-1);
                List<TreeNode_95> rightListHead = find(headVal+1, end);
                for(TreeNode_95 left : leftListHead){
                    for(TreeNode_95 right : rightListHead){
                        TreeNode_95 tmp = new TreeNode_95(headVal);
                        tmp.left = left;
                        tmp.right = right;
                        result.add(tmp);
                    }
                }
            }
        }
        return result;
    }


    public static void main(String[] args) {
        Solution_95 base = new Solution_95();
        base.generateTrees(3);
    }
}