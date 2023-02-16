package Leetcode;
import java.util.*;

public class Arrays{
    static void ShiftArrayLeft(int[] array, int number){
        int notempty = 0;
        for (int i = 0; i < array.length; i++){
            array[i] = i;
            notempty ++;
        }
        notempty--;
        //shifting array
        int position = number - 1;
        for (int i = 0; i <= position; i++){
            array[i] = 0;
        }

        for (int i = number; i < array.length; i++){
            array[i-number] = array[i];
        }

        int counter = 0;
        for (int i = array.length - 1; counter < number; i--){
            array[i] = 0;
            counter += 1;
        }

    }

    static int removeElement(int[]nums, int val){
        int count = 0;
        int ccount = 0;
        int proper = 0;
        boolean equal = true;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == val){
                nums[i] = 51;
                count ++;
            }
            else{
                equal = false;
            }
        }
        
        boolean Condition = true;
        int i = 0; //start
        int j = nums.length-1; //end
        while (ccount != count){
            if (equal == true){
                ccount = count;
            }

            else if (i == j){
                break;
            }

            else{
                if(nums[i] != 51){
                    i++;
                }
                else if (nums[i] == 51){
                    if (nums[j] == 51){
                        j--;
                    }
                    else{
                        int temp = nums[i];
                        nums[i] = nums[j];
                        nums[j] = temp;
                        i++;
                        j = nums.length-1;
                        ccount++;
                    }
                }
            }
           

        }

        for (int s : nums){
            if (s != 51){
                proper++;
            }
        }
        return proper;
    }

    public static void main (String args[]){
        int [] a1 = new int[10];
        int[] a2 = {0,1,2,2,3,0,4,2};

        System.out.println(removeElement(a2,2));
        for (int i : a2){
            System.out.println(i);
        }
        
    }
}