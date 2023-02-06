package Leetcode;
import java.util.*;
import java.lang.Math;

public class ReverseInt{

    public int reverse(int x){
        double low = -Math.pow(2,31);
        double high = (Math.pow(2,31)) - 1;
        StringBuilder answer = new StringBuilder();
        String intstring = String.valueOf(x);
        int nlength = intstring.length();
        String placeholder = String.valueOf(intstring.charAt(0));
        if (placeholder.equals("-")){
            answer.insert(0,"-");
        }
        for (int i = nlength-1, j = 0; i >= 0;){
            String digit = String.valueOf(intstring.charAt(i));
            if (digit.equals("-")){i--;}
            else{
                answer.append(digit);
                j++;
                i--;
            }
        }

        
        String final2 = answer.toString();
       
    
        if(Long.parseLong(final2) > high || Long.parseLong(final2) < low){
            return 0;
        }

        else{
            int final1 = Integer.parseInt(final2);
            return final1;
        }
    }


    public static void main (String args[]){
        ReverseInt Test = new ReverseInt();
        String string = "-214";
        double high = (Math.pow(2,31)) - 1;
        //System.out.print(high > 9646324351L);
        System.out.print(Test.reverse(1534236469));
    }
}