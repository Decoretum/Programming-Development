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
     * Complete the 'hourglassSum' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY arr as parameter.
     */

    public static int hourglassSum(List<List<Integer>> arr) {
    ArrayList<Integer> Sums = new ArrayList<>();
    int Sum = 0, i=0, j=0, k=0;
    while (i < 4){
        int babysum = 0;
        babysum += (arr.get(i).get(j) + arr.get(i).get(j+1) + arr.get(i).get(j+2));   
        babysum += arr.get(i+1).get(j+1);
        babysum += (arr.get(i+2).get(j) + arr.get(i+2).get(j+1) + arr.get(i+2).get(j+2));
        j++;
        Sums.add(babysum);
        
        if (j == 4){
            i++;
            j=0;
        }
    }

    return Collections.max(Sums);
    }

}
