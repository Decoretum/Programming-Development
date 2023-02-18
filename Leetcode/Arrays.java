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

    static int removeDuplicates(int[] nums){
        //pointers
        ArrayList<Integer> nodup = new ArrayList<>();
        int i = 0;
        int j = 0;
        int k = 0;
        int len = nums.length;
        while(j < len){
            if (nodup.contains(nums[j]) == false){
                nodup.add(nums[j]);      //when adding with hashset, elements added aren't retaining their order of adding       
                i++;
                j++;
            }
            else{
                nums[j] = 101;
                j++;
            }
        }

        //reuse them
        i = 0;
        j = 0;


        for (int l : nodup){
            if (k < nodup.size()){
                nums[k] = l;
                k++;
            }
        }

        while (k < len){
            nums[k] = 101;
            k++;
        }

        return nodup.size();
    }

    //Edge cases - scenarios that you wouldn't expect to encounter, extremities, oddities

    static boolean checkIfExist(int[] arr){
        boolean cond = false;
        int i = 0;
        int j = 1;
        if (arr == null){
            return false;
        }

        else{
            while (i < arr.length && j < arr.length){
                if (i != j && arr[i] == 2 * arr[j]){
                    cond = true;
                    break;
                }
                
                else{
                    if (j == arr.length - 1){
                        i++;
                        j = 0;
                    }
                    else{
                        j++;
                    }  
                }     
            }
        }
        return cond;
    }

    static boolean validMountainArray(int[] arr) {
        boolean cond = true;
        boolean odd = false;
        boolean inc = false;
        boolean dec = false;
        int i = 0;
        int back = -1; //element before arr[i]

        if (arr.length < 3){
            return false;
        }
        
        else{
            while(i < arr.length - 1){
                if (arr[i] < arr[i+1] && dec == false){
                    i++;
                    inc = true;
                }
                else if (arr[i] > arr[i+1]){
                    i++;
                    dec= true;
                }
                else if (arr[i] < arr[i+1] && dec == true ){
                    return false;
                }
                else if (arr[i] == arr[i+1]){
                    return false;
                }
            }
        }
        if (dec == true && inc == true){
            cond = true;
        }
        else{
            cond = false;
        }
        return cond;
    }

    public static void main (String args[]){
        int [] a1 = new int[10];
        int[] a2 = {9,8,7,6,5,4,3,2,1,0};

        //System.out.println(removeElement(a2,2));
        //removeDuplicates(a2);
        //System.out.println(checkIfExist(a2));
        System.out.println(validMountainArray(a2));
        for (int i : a2){
            System.out.println(i);
        }
        
    }
}