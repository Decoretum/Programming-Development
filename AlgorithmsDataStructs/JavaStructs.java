package AlgorithmsDataStructs;
import java.util.*;

public class JavaStructs{
    public static void main (String args[]){
        Stack<String> my = new Stack<>();
        my.push("Gael");
        my.push("You");
        my.push("Dame");
        my.push("Sand");
        String popped = my.pop();
        String peeking = my.peek();
        System.out.println(peeking);
        System.out.println(my.search("You"));
        System.out.println(6 % 10);
    }
}

/*

*/