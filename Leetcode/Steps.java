class Solution {
    public int numberOfSteps(int num) {
        int reference = num;
        int step = 0;
        while (reference != 0){
            if (reference % 2 == 0){
                reference = reference / 2;
                step += 1;
            }
            else{
                reference -= 1;
                step += 1;
            }
        }
        return step;
        
    }
}