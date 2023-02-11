class Solution {
    public int maximumWealth(int[][] accounts) {
        int [] sum = new int[accounts.length];
        for (int i = 0; i < accounts.length; i++){
            for (int j = 0; j < accounts[i].length; j++){
                sum[i] = sum[i] + accounts[i][j];
            }
        }
        int best = 0;
        for (int i : sum){
            if(i > best){
                best = i;
            }
        }
        return best;
    }
}