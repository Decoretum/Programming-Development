package Leetcode;
import java.util.*;

class Solution {
    static void SelectionSort(int[]array){
        for (int i = 0; i < array.length; i++){
            int min = i;
            for (int k = i+1; k < array.length; k++){
                if (array[k] <= array[min]){
                    min = k;
                }
            
            }
            int temp = array[i];
            array[i] = array[min];
            array[min] = temp;
    
        }
    }
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = 0; //pointer for nums1
        int j = 0; //pointer for nums2
        for (; j < nums2.length; i++){
            if (nums1[i] == 0){
                nums1[i] = nums2[j];
                j++;
            }
        }
        for (int o : nums1){
            System.out.println(o);
        }
        SelectionSort(nums1);
        
    }
}