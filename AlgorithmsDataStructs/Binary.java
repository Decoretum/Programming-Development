package AlgorithmsDataStructs;
import java.util.*;

public class Binary {
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

    static long NtoDec(int N,long a){
        String A = Long.toString(a); 
        long [] Bits = new long[A.length()];
        for (int i = A.length() - 1, j = 0; i >= 0; i--, j++){
            Bits[j] = Long.valueOf(String.valueOf(A.charAt(i)));
        }

        long sum = 0;

        for (int i = 0; i <= Bits.length - 1; i ++){
            long val = Bits[i] * (int) Math.pow(N, i);
           
            sum += val;
      
        }

        return sum;
    }

    static long Convert(ArrayList<Long> array){
        String num = "";
        for (int i=0; i < array.size(); i++){
            num += array.get(i);
        }
        long final1 = Long.parseLong(num);
        return final1;
    }

    static void BinaryAddition(ArrayList <ArrayList<Long>> array1){
        ArrayList<Long> Total = new ArrayList<>();
        for (int i = 0; i < array1.size(); i++){
            Total.add(NtoDec(2,Convert(array1.get(i))));
        }

        long sum = 0;
        for (int i = 0; i < Total.size(); i++){
            sum += Total.get(i);
        }
        /*int sum = array1.get(i) + array2.get(i) + carry;
        result[i+1] = sum % 2;
        carry = sum / 2; 

        result[0] = carry; 
        for (int i : result){
            System.out.print(i);
        } */
        System.out.println(sum);
    }



    static void BinaryMult(int array1[], int array2[]){
        ArrayList <ArrayList<Long>> Total = new ArrayList<>();
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
            ArrayList <Long> First = new ArrayList<>();
            String ans1 = "";
            for (int j = multiplicand.length - 1; j >= 0; j--){
                ans1 += Integer.toString(lastdigit * multiplicand[j]);
            }
            for (int k = ans1.length() - 1; k >= 0; k--){
                First.add(Long.parseLong(Character.toString(ans1.charAt(k))));
            }
            /* Use case for classic placeholder */
            if (i < multiplier.length - 1){
                long remaining = (multiplier.length - 1) - i;
                for (int j = 1; j <= remaining; j++){
                    First.add(0L);
                }
            } 

            Total.add(First);
        }

        int totallength = Total.get(Total.size()-1).size();
            for (int l = 0; l < Total.size()-1; l++){
                if (Total.get(l).size() != totallength){
                    int difference = totallength - Total.get(l).size();
                    for (int m = 1; m <= difference; m++){
                        Total.get(l).add(0,0L);
                    }
                }
            }
        BinaryAddition(Total);
        
    }
    public static void main (String args[]){
        int one [] = {0,1,0,1};
        int two [] = {1,1,1,0};
        //BinaryAddition(one,two);
        BinaryMult(one,two);

    }
}