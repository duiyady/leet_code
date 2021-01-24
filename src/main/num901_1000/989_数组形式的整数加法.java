package num901_1000;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
 给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。 

 示例 1：
 输入：A = [1,2,0,0], K = 34
 输出：[1,2,3,4]
 解释：1200 + 34 = 1234
*/

class Solution_989 {
    public List<Integer> addToArrayForm(int[] A, int K) {
        int jin = 0;
        int now = 0;
        List<Integer> result = new LinkedList<>();
        for(int i = A.length-1; i>=0; i--){
            now = (A[i] + K%10 + jin)%10;
            jin = (A[i] + K%10 + jin)/10;
            K = K/10;
            result.add(0, now);
        }
        while (K != 0){
            now = (K%10 + jin)%10;
            jin = (K%10 + jin)/10;
            K = K/10;
            result.add(0, now);
        }
        if(jin != 0){
            result.add(0, jin);
        }
        return result;
    }
}
