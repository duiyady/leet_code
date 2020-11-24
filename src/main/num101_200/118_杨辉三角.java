import java.util.ArrayList;
import java.util.List;

class Solution {
    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>(numRows);
        for(int i = 0; i < numRows; i++){
            List<Integer> tmp = new ArrayList<>(i+1);
            tmp.add(1);
            if(i>0) {
                for (int j = 1; j < i; j++) {
                    tmp.add(result.get(i-1).get(j - 1) + result.get(i-1).get(j));
                }
                tmp.add(1);
            }
            result.add(tmp);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(generate(4));
    }
}