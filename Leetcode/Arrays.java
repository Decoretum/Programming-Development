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
    public static void main (String args[]){
        int [] a1 = new int[10];
        for (int i = 0; i < a1.length; i++){
            a1[i] = i;
        }
        ShiftArrayLeft(a1,4); //2 elements shifted
        for (int i : a1){
            System.out.println(i);
        }

    }
}