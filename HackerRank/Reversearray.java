import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'reverseArray' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts INTEGER_ARRAY a as parameter.
     */

    public static List<Integer> reverseArray(List<Integer> a) {
    if (a.size() % 2 == 0){
        int i = 0, j = a.size()-1;
        for (; ; i++,j--){
            int tempa = a.get(i);
            a.set(i,a.get(j));
            a.set(j,tempa);
            if (i == j-1){
                return a;
            }
        }
        
    }
    else{
        int mid = a.size() / 2;
        int i = 0, j = a.size()-1;
        for (; i != mid; i++, j--){
            int temp = a.get(i);
            a.set(i, a.get(j));
            a.set(j, temp);
        }
    }
    return a;
    }

}