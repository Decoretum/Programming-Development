package Leetcode;
import java.util.*;

public class FizzBuzz{
    public ArrayList<String> fizzBuzz(int n){
        ArrayList<String> Answer = new ArrayList<>();
        for (int i = 0; i < n; i++){
            int sum = i+1;
            if ( (sum / 3 != 0 && sum / 5 != 0) && (sum % 3 == 0 && sum % 5 == 0) ){
                Answer.add("FizzBuzz");
            }
            else if (sum / 3 != 0 && sum % 3 == 0){
                Answer.add("Fizz");
            }
            else if (sum / 5 != 0 && sum % 5 == 0){
                Answer.add("Buzz");
            }
            else{
                Answer.add(String.valueOf(i+1));
            }
        }
        return Answer;
    }

    public static void main (String args[]){
        FizzBuzz test = new FizzBuzz();
        System.out.print(test.fizzBuzz(5));
    }
}