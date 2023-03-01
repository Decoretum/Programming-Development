class Solution {
    public int searchInsert(int[] nums, int target) {
        //binary search
        int pos = 0;
        if (!Arrays.asList(nums).contains(target) == true){
            for (int val=0; val < nums.length; val++){
                if (val != nums.length - 1 && target > nums[val] && target < nums[val+1]){
                    return pos = val + 1;
                }
                else if (val == 0 && target < nums[val]){return pos = 0;}
                else if (val == nums.length - 1 && target > nums[val]){return pos = val + 1;}
            }
        }

        int high = nums.length - 1;
        int low = 0;
        int middle = 0;
        boolean found = false;
        while (high != low){
            middle = (low + high) / 2;
            if (nums[low] == target){return low;}
            
            else if (nums[high] == target){return high;}

            if (nums[middle] > target){
                high = middle - 1;
            }
            else if (nums[middle] < target){
                low = middle + 1;
            }
            if (nums[middle] == target){
                found = true;
                return middle;
            }
        }
        if (found == true){return middle;}
        else{return pos;}
    }
}