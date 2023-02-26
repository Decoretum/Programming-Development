package Leetcode;
import java.util.*;

class Solution {
     public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        int i = 0;
        int j = nums.length - 1;

         if (nums.length == 1){
            ans[0] = nums[0];
            return ans;
        }

        else if (nums.length == 2){
            if (nums[i] + nums[j] == target){
                ans[0] = i;
                ans[1] = j;
            }
            else{
                return ans;
            }
        }

        else if (nums.length > 2){

            for (; i < nums.length;){
             if (nums[i] + nums[j] == target && i != j){
                    ans[0] = i;
                    ans[1] = j;
                    return ans;
                }
                else{
                    if (j > 0) j--;
                    else if (j == 0){
                        j = nums.length-1;
                        i++;
                    }
                
            }
    }

        }
        return ans;
    }
}