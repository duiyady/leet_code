import java.util.ArrayList;
import java.util.List;

/**
 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
 返回 s 所有可能的分割方案。

 示例:
 输入: "aab"
 输出:
 [
 ["aa","b"],
 ["a","a","b"]
 ]
 */

class Solution_131 {
    List<List<String>> result = new ArrayList<>();
    List<String> tmp = new ArrayList<>();
    char[][] huiFlag;
    public List<List<String>> partition(String s) {
        char[] ch = s.toCharArray();
        huiFlag = new char[ch.length][ch.length];
        deal(0, ch);
        return result;
    }

    public void deal(int index, char[] s){
        if(index == s.length){
            List<String> tt = new ArrayList<>(tmp);
            result.add(tt);
        }else {
            for(int j = s.length-1; j >= index; j--){
                if(huiFlag[index][j] == 't'){
                    tmp.add(String.valueOf(s, index, j+1-index));
                    deal(j+1, s);
                    tmp.remove(tmp.size()-1);
                }else if(huiFlag[index][j] == 'f'){

                }else {
                    int start = index;
                    int end = j;
                    boolean ishui = true;

                    while (start < end) {
                        if (s[start] != s[end]) {
                            ishui = false;
                            break;
                        } else {
                            start++;
                            end--;
                        }
                    }

                    if (ishui) {
                        tmp.add(String.valueOf(s, index, j + 1 - index));
                        huiFlag[index][j] = 't';
                        deal(j + 1, s);
                        tmp.remove(tmp.size() - 1);
                    } else {
                        huiFlag[index][j] = 'f';
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        String s = "aacc";

        List<List<String>> tm = new Solution_131().partition(s);
        System.out.println(tm);
    }
}