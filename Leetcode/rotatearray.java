class Solution {
    public void rotate(int[] nums, int k) {
        if (nums.length <= 3){}
        else{
            int loopfront = 0;
            int loopback = 0;
            int[] container = new int[k];
            for (int i = nums.length-k, j =0; i < nums.length; i++,j++){
                container[j] = nums[i];
                nums[i] = 0;
            }

            for (int i = nums.length-k-1, j=nums.length-1; i >= 0; i--,j--){
                nums[j] = nums[i];
            }

            for (int i = 0, j=0; i < k; i++,j++){
                nums[i] = container[j];
            }   
        }
        
        
    }
}
