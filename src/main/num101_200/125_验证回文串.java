/**
 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
 说明：本题中，我们将空字符串定义为有效的回文串。

 示例 1:
 输入: "A man, a plan, a canal: Panama"
 输出: true

 示例 2:
 输入: "race a car"
 输出: false
 */

class Solution_125 {
    public static boolean isPalindrome(String s) {
        char[] a = s.toLowerCase().toCharArray();
        int i = 0;
        int j = a.length - 1;
        while (i < j){
            if(!((a[i] >= 'a' && a[i] <= 'z') || (a[i] >= '0' && a[i] <= '9'))){
                i += 1;
                continue;
            }
            if(!((a[j] >= 'a' && a[j] <= 'z') || (a[j] >= '0' && a[j] <= '9'))){
                j -= 1;
                continue;
            }
            if(a[i] != a[j]){
                return false;
            }
            i += 1;
            j -= 1;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome("A man, a plan, a canal: Panama"));
    }
}