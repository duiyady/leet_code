//给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

import java.util.ArrayList;
import java.util.List;

class Solution_119 {
    public static List<Integer> getRow(int rowIndex) {
        if(rowIndex < 0){
            return null;
        }
        List<Integer> result = new ArrayList<>(rowIndex+1);
        for(int i = 0; i <= rowIndex; i++){
            result.add(i, 1);
            for(int j = i-1; j > 0; j--){
                result.set(j, result.get(j)+result.get(j-1));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(getRow(4));
    }
}