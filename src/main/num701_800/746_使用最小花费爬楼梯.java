import com.sun.tools.javac.Main;

class Solution_746 {
    public int minCostClimbingStairs(int[] cost) {
        if(cost.length == 0){
            return 0;
        }else if(cost.length == 1){
            return cost[0];
        }else if(cost.length == 2){
            return cost[1];
        }else {
            for(int i = 2; i < cost.length; i++){
                cost[i] += Math.min(cost[i-1], cost[i-2]);
            }
            return Math.min(cost[cost.length-1], cost[cost.length-2]);
        }
    }

}