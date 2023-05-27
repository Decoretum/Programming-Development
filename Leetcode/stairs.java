import java.util.*;

public class stairs{
    static HashMap<Integer,Integer> hm = new HashMap<>();

    static int fib(int a){
        if (hm.containsKey(a)){
            return hm.get(a);
        }
        if (a <= 3){
            switch(a){
            case 1:
                return 1;
            case 2:
                return 2;
            case 3:
                return 3;
        }
       
    }  
        else {
            //memoizing
            int result = fib(a-1) + fib(a-2);
            // System.out.println(result);
            hm.put(a, result);
            return fib(a-1) + fib(a-2);
        }   
        return 0;
    }
    public static void main (String args[]){
        System.out.println(fib(45));
    }
}