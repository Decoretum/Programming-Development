package AlgorithmsDataStructs;
import java.util.*;

public class Binary{
    static void BinaryAddition(int array1[], int array2[]){
        int result[] = new int[array1.length + 1]; 
        int carry = 0;
        for (int i = array1.length-1; i >= 0; i--){
            int sum = array1[i] + array2[i] + carry;
            result[i+1] = sum % 2;
            carry = sum / 2;
        }
        result[0] = carry;
        for (int i : result){
            System.out.print(i);
        }
        System.out.println("");
    }

    static void BinaryMult(int array1[], int array2[]){
        ArrayList <ArrayList<Integer>> Total = new ArrayList<>();
        int multiplicand [];
        int multiplier [];
        if (array1.length > array2.length){
            multiplicand = array1;
            multiplier = array2;
        }
        else{
            multiplicand = array2;
            multiplier = array1;
        }

        for (int i = multiplier.length-1; i >= 0; i--){
            int lastdigit = multiplier[i];
            ArrayList <Integer> First = new ArrayList<>();
            String ans1 = "";
            for (int j = multiplicand.length - 1; j >= 0; j--){
                ans1 += Integer.toString(lastdigit * multiplicand[j]);
            }
            for (int k = 0; k < ans1.length(); k++){
                First.add(Integer.parseInt(Character.toString(ans1.charAt(k))));
            }
            Total.add(0,First);

        }
        System.out.println(Total);
    }
    public static void main (String args[]){
        int one [] = {1,0,1,0,1,0,1,0};
        int two [] = {1,1,0,0,1,1,0,0};
        BinaryAddition(one,two);
        BinaryMult(one,two);

    }
}