package AlgorithmsDataStructs;
import java.util.*;

public class Alg7 {

    static void Swap(String a, String b){
        String A1 = a;
        String A2 = b;
        System.out.println("a: " + A1 + ". b: " + A2);
        String temp;

        temp = A1;
        A1 = A2;
        A2 = temp;

        System.out.println(A1 + " and " + A2);
    }

    static void Robot(){
        System.out.println("+\"\"\"\"\"+");
        System.out.println("[ |  o o  | ]");
        System.out.println("  |   ^   |  ");
        System.out.println("  | ' _ ' |  ");
        System.out.println("  + ----- +  ");

    }

    static void NtoDec(int N,int a){
        String A = Integer.toString(a); 
        int [] Bits = new int[A.length()];
        double [] Converted = new double[Bits.length];
        for (int i = A.length() - 1, j = 0; i >= 0; i--, j++){
            Bits[j] = Integer.parseInt(String.valueOf(A.charAt(i)));
        }

        double sum = 0;

        for (int i = 0; i <= Bits.length - 1; i ++){
            double val = Math.pow(N, i);
            if (Bits[i] == 1){
                Converted[i] = val;
                sum += Converted[i];
            }
        }

        System.out.println(sum);
    }

    static void DectoN(int N, int a){
        ArrayList <Integer> Digits = new ArrayList<>();
        int dig = a;
        while (dig != 0){
            Digits.add(dig % N);
            dig = dig/N;
        }
        Collections.reverse(Digits);
        System.out.println(Digits);
    }

    public static void main(String args[]){
        double result = ((25.5 * 3.5) - (3.5*3.5)) / (40.5 - 4.5);
        double result1 = 4.0 * (1-(1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11));
        double perimeter = (2 *  Math.PI) * 7.5;
        double carea = (Math.PI * (Math.pow(7.5, 2)));
        
        System.out.println(result);
        System.out.println(result1);
        System.out.println(perimeter);
        System.out.println(carea);
        Swap("you","me");
        Robot();
        //BinarytoDec(110110110); //230167
        DectoN(11,2003);
        NtoDec(7, 101011111);
    }
}
