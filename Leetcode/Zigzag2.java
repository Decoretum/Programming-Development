package Leetcode;
import java.util.*;

public class Zigzag2 { //This is my attempt after learning how the String traversal algorithm works

    static String convert(String s, int numRows){
        if (numRows == 1){
            return s;
        }

        StringBuilder final1 = new StringBuilder();
        int stringlength = s.length();
        int charsinsection = (2 * numRows) - 2;

        //traverse vertically per row
        for (int row = 0; row < numRows; row++){
            int rowindex = row;
            //here, we traverse different sections per row
            while (rowindex < stringlength){
       
                final1.append(s.charAt(rowindex));
                if (row != 0 && row != numRows - 1){
                    int charsbetween = charsinsection - (2 * row); //characters same row between different sections
                    int nextindex = rowindex + charsbetween;
                    if (nextindex < stringlength){
                        final1.append(s.charAt(nextindex));
                    }
                }

                rowindex += charsinsection;
            }
        }


        return final1.toString();
    }

    public static void main (String args[]){
        String test = "PAYPALISHIRING";
        System.out.println(convert(test,3));
    }
}