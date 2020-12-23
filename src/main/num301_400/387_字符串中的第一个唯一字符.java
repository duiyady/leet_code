import java.util.ArrayList;
import java.util.List;

/**
 * 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
 *
 * 示例：
 * s = "leetcode"
 * 返回 0
 * s = "loveleetcode"
 * 返回 2
 */

class Solution_387 {
    public int firstUniqChar(String s) {
        int result = s.length();
        for (char c = 'a'; c <= 'z' ; c++) {
            int firstIndex = s.indexOf(c);
            int lastIndex = s.lastIndexOf(c);

            //如果相等表示不重复
            if(lastIndex == firstIndex && firstIndex != -1 ){
                result = Math.min(firstIndex,result);
            }
        }
        if(result != s.length()){
            return result;
        }
        return -1;
    }


    public static void main(String[] args) {
        System.out.println(new Solution_387().firstUniqChar("abdadaad"));
    }
}