package Leetcode;
import java.util.*;

public class RomantoInt{
    static int romanToInt(String s){
        HashMap <String,Integer> Code = new HashMap <>();
        Code.put("I",1);
        Code.put("V",5);
        Code.put("X",10);
        Code.put("L",50);
        Code.put("C",100);
        Code.put("D",500);
        Code.put("M",1000);
        int sum = 0;
        int i = 0;
        while (i < s.length()){
            if (i+1 <= s.length() - 1){
                String current = String.valueOf(s.charAt(i));
                String next = String.valueOf(s.charAt(i+1));
                if ((current.equals("I"))){
                    if (next.equals("V")){
                        sum += 4;
                        i += 2;
                    }

                    else if (next.equals("X")){
                        sum += 9;
                        i += 2;
                    }

                    else {
                    sum += Code.get(String.valueOf(s.charAt(i)));
                    i += 1;
                 }
                 }

                 else if (current.equals("X")){
                    if (next.equals("L")){
                        sum += 40;
                        i += 2;
                    }

                    else if (next.equals("C")){
                        sum += 90;
                        i += 2;
                    }

                    else {
                    sum += Code.get(String.valueOf(s.charAt(i)));
                    i += 1;
                 }
                 }

                 else if (current.equals("C")){
                    if (next.equals("D")){
                        sum += 400;
                        i += 2;
                    }

                    else if (next.equals("M")){
                        sum += 900;
                        i += 2;
                    }

                    else {
                    sum += Code.get(String.valueOf(s.charAt(i)));
                    i += 1;
                 }
                 }

            else {
                sum += Code.get(String.valueOf(s.charAt(i)));
                i += 1;
            }
            }

            else {
                    sum += Code.get(String.valueOf(s.charAt(i)));
                    i += 1;
                 }
            
            
        }
        return sum;
    }

    public static void main (String args[]){
        System.out.println(romanToInt("III"));
    }
}