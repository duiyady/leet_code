import java.util.*;

/**
 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
 每次转换只能改变一个字母。
 转换过程中的中间单词必须是字典中的单词。
 说明:
 如果不存在这样的转换序列，返回 0。
 所有单词具有相同的长度。
 所有单词只由小写字母组成。
 字典中不存在重复的单词。
 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
 示例 1:
 输入:
 beginWord = "hit",
 endWord = "cog",
 wordList = ["hot","dot","dog","lot","log","cog"]
 输出: 5
 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 返回它的长度 5。

 示例 2:
 输入:
 beginWord = "hit"
 endWord = "cog"
 wordList = ["hot","dot","dog","lot","log"]
 输出: 0
 解释: endWord "cog" 不在字典中，所以无法进行转换。
 */

class Solution_127 {
    public static int ladderLength(String beginWord, String endWord, List<String> wordList) {
        int startId=-1, endId=-1;
        List<Integer>[] adjDict = new List[wordList.size() + 1];
        for(int i = 0; i < adjDict.length; i++){
            adjDict[i] = new ArrayList<>();
        }

        for(int i = 0; i < wordList.size(); i++){
            if (wordList.get(i).equals(endWord)){
                endId = i;
            }else if(wordList.get(i).equals(beginWord)){
                startId = i;
            }
            for(int j = i+1; j < wordList.size(); j++){
                int k = 0, count = 0;
                while (k < wordList.get(i).length() && count < 2){
                    if(wordList.get(i).charAt(k) != wordList.get(j).charAt(k)){
                        count++;
                    }
                    k++;
                }
                if(count == 1){
                    adjDict[i].add(j);
                    adjDict[j].add(i);
                }
            }
        }

        if (endId == -1){
            return 0;
        }
        if (startId == -1) {
            wordList.add(beginWord);
            startId = wordList.size()-1;
            for(int i = 0; i < wordList.size() - 1; i++){
                int k = 0, count = 0;
                while (k < wordList.get(i).length() && count < 2){
                    if(wordList.get(i).charAt(k) != wordList.get(startId).charAt(k)){
                        count++;
                    }
                    k++;
                }
                if(count == 1){
                    adjDict[i].add(startId);
                    adjDict[startId].add(i);
                }
            }
        }


        List<Integer> delList = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(startId);
        queue.offer(-1);
        Integer now;
        int step = 0;
        while (queue.size() > 0){
            now = queue.poll();
            if(now == -1){
                step += 1;
                if (queue.size() == 0){
                    return 0;
                }else {
                    queue.offer(-1);
                }
            }else if(now == endId){
                return step+1;
            }else if(!delList.contains(now)) {
                delList.add(now);
                for (Integer val : adjDict[now]) {
                    if (!delList.contains(val)){
                        queue.offer(val);
                    }
                }
            }
        }

        return 0;
    }

    public static void main(String[] args) {
//        List<String> list = new ArrayList<String>(Arrays.asList("hot","dot","dog","lot","log","cog"));
        List<String> list = new ArrayList<String>(Arrays.asList("hot","dog"));

        System.out.println(ladderLength("hot", "dog", list));
    }
}