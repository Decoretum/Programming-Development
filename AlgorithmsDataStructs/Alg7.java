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
        for (int i = A.length() - 1, j = 0; i >= 0; i--, j++){
            Bits[j] = Integer.parseInt(String.valueOf(A.charAt(i)));
        }

        int sum = 0;

        for (int i = 0; i <= Bits.length - 1; i ++){
            int val = Bits[i] * (int) Math.pow(N, i);
           
            sum += val;
      
        }

        System.out.println(sum);
    }

    static void DectoN(int N, int a){
        ArrayList <Integer> Digits = new ArrayList<>();
        String finalint = "";
        int dig = a;
        while (dig != 0){
            Digits.add(dig % N);
            dig = dig/N;
        }
        Collections.reverse(Digits);
        for (int d : Digits){
            finalint += Integer.toString(d);
        }

        System.out.println(finalint);
    }

    static void NtoN(int N1, int N2, int Num){
        String finalint = "";
        String A = Integer.toString(Num); 
        int [] Bits = new int[A.length()];
        for (int i = A.length() - 1, j = 0; i >= 0; i--, j++){
            Bits[j] = Integer.parseInt(String.valueOf(A.charAt(i)));
        }

        int sum = 0;

        for (int i = 0; i <= Bits.length - 1; i ++){
            double val = Bits[i] * Math.pow(N1, i);
            sum += val;
        }


        

        ArrayList <Integer> Digits = new ArrayList<>();
        while (sum != 0){
            Digits.add(sum % N2);
            sum = sum/N2;
        }

        Collections.reverse(Digits);
        for (int x = 0; x <= Digits.size()-1; x++){
            finalint += Integer.toString(Digits.get(x));
        }

        System.out.println(finalint);

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
        DectoN(2, 5);
        DectoN(8, 15);
        NtoDec(2, 100);
        NtoN(2,8,111);
        NtoDec(8, 10);
        NtoN(8,10,10);
        DectoN(2,2);
      
      
    }

    
}
