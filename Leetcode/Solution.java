package Leetcode;
import java.util.*;
import java.io.FileNotFoundException;

//Was able to do whole Merge sort without external help/guide
class Solution {
    static void MergeSort(int[]array){
        int length = array.length;
        int middle = length / 2;
        int left[] = new int[middle];
        int right[] = new int[length-middle];
        //2 pointers
        int i = 0; //left
        int j = 0; //right

        if (length == 1){
            return;
        }
        
        while (i < middle){
            left[i] = array[i];
            i++;
        }
        
        while (j < right.length){
            right[j] = array[i];
            j++;
            i++;
        }
        
        MergeSort(left);
        MergeSort(right);
        Merge(array,left,right);
    }
    
    static void Merge(int[]array, int[] left, int[] right){
        int length = array.length;
        int leftl = left.length;
        int rightl = right.length;
        
        int i = 0; //left
        int j = 0; //right
        int k = 0; //for main array
        
        while (i < leftl && j < rightl){
            if (left[i] < right[j]){
                array[k] = left[i];
                i++;
                k++;
            }
            else if (left[i] > right[j]){
                array[k] = right[j];
                j++;
                k++;
            }
            else if (left[i] == right[j]){
                array[k] = left[i];
                array[k+1] = right[j];
                i++;
                j++;
                k+=2;
            }
        }
        
        while (i < leftl){
            array[k] = left[i];
            k++;
            i++;
        }
        
        while (j < rightl){
            array[k] = right[j];
            k++;
            j++;
        }
    }
    public int[] sortedSquares(int[] nums) {
        for (int i : nums){
            nums[i] = i * i;
        }
        MergeSort(nums);
        return nums;
        
    }

    public static void main (String[]args){
        int[] nums = {-7,-3,2,3,11};
        for (int i =0; i< nums.length; i++){
            nums[i] = nums[i] * nums[i];
        }
        for (int i : nums){
            System.out.println(i);
        } 
        MergeSort(nums);
        
        for (int i : nums){
            System.out.println(i);
        }        
    }
}