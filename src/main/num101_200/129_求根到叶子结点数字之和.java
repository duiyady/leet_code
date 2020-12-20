import java.util.ArrayList;
import java.util.List;

/**
 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
 例如，从根到叶子节点路径 1->2->3 代表数字 123。
 计算从根到叶子节点生成的所有数字之和。
 说明: 叶子节点是指没有子节点的节点。

 示例 1:
 输入: [1,2,3]
 1
 / \
 2   3
 输出: 25
 解释:
 从根到叶子节点路径 1->2 代表数字 12.
 从根到叶子节点路径 1->3 代表数字 13.
 因此，数字总和 = 12 + 13 = 25.

 示例 2:
 输入: [4,9,0,5,1]
 4
 / \
 9   0
  / \
 5   1
 输出: 1026
 解释:
 从根到叶子节点路径 4->9->5 代表数字 495.
 从根到叶子节点路径 4->9->1 代表数字 491.
 从根到叶子节点路径 4->0 代表数字 40.
 因此，数字总和 = 495 + 491 + 40 = 1026.
 */

//class TreeNode {
//      int val;
//      TreeNode left;
//      TreeNode right;
//      TreeNode(int x) { val = x; }
//  }

class Solution_129 {
    public static int sumNumbers(TreeNode root) {
        if(root == null){
            return 0;
        }
        int now = 0;
        int result = 0;
        List<TreeNode> list = new ArrayList<>();
        List<Integer> state = new ArrayList<>();
        list.add(root);
        state.add(0);
        now = root.val;
        while (list.size() > 0){
            int s = state.get(state.size()-1);
            TreeNode node = list.get(list.size() - 1);
            if(s == 0){
                if(node.left != null){
                    state.set(state.size()-1, 1);
                    list.add(node.left);
                    now = now*10 + node.left.val;
                    state.add(0);
                }else if(node.right != null){
                    state.set(state.size()-1, 2);
                    list.add(node.right);
                    now = now*10 + node.right.val;
                    state.add(0);
                }else {
                    result += now;
                    now = (now - node.val)/10;
                    list.remove(list.size() - 1);
                    state.remove(state.size() - 1);
                }
            }else if(s == 1){
                if(node.right != null){
                    state.set(state.size()-1, 2);
                    list.add(node.right);
                    now = now*10 + node.right.val;
                    state.add(0);
                }else {
                    now = (now - node.val)/10;
                    list.remove(list.size() - 1);
                    state.remove(state.size() - 1);
                }
            }else {
                now = (now - node.val)/10;
                list.remove(list.size() - 1);
                state.remove(state.size() - 1);
            }
        }


        return result;
    }

    public static void main(String[] args) {
        TreeNode a = new TreeNode(1);
        TreeNode b = new TreeNode(2);
        TreeNode c = new TreeNode(3);
        a.left = b;
        a.right = c;
        System.out.println(sumNumbers(a));


    }
}