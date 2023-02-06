package Leetcode;
import java.util.*;

//My attempt at this annoying Leetcode solution, unfinished
public class Zigzag{
    static void Convert(String s, int numRows){ //numRows also determine no. of values per columns
        int columns = s.length() / numRows; //number of columns
        int space = numRows - 2; //number of in between values
        ArrayList<ArrayList<String>> Columns = new ArrayList<>();
        ArrayList<String> Spaces = new ArrayList<>();
        for (int i = 0; i < columns; i++){
            ArrayList<String> samp = new ArrayList<>();
            Columns.add(samp);
        }
        int i = 0; //counter for whole string length
        int j = 0; //counter for column value
        int k = 0; //counter for what column
        int l = 0; //counter for spaces
        
        while (i < s.length() && k < Columns.size()){
            if (Columns.get(k).size() < numRows){
                Columns.get(k).add(String.valueOf(s.charAt(i)));
                i++;
            }
            else{
                if (l < space){
                    Spaces.add(String.valueOf(s.charAt(i)));
                    i++;
                }
                k++;
                l = 0;
                i = i + space + 1;
            }
        }

        System.out.println(Columns);
        System.out.println(Spaces);
        }
    
    public static void main (String args[]){
        Convert("PAYPALISHIRING",3);
    }

}