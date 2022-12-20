package LearnJava;
import java.lang.Math;
import java.util.*;

public class Maths {

    static void Hypotenuse(){
        Scanner input = new Scanner(System.in);
        System.out.println("Input x: ");
        double x = input.nextDouble();
        System.out.println("Input y: ");
        double y = input.nextDouble();
        double answer = Math.sqrt((x*x) + (y*y));
        System.out.println(String.format("The hypotenuse is %f",answer));
        input.close();
    }
    public static void main (String args[]){
        double a = 1;
        double b = 2;
        int c = -50;
        System.out.println(Math.max(a,b));
        System.out.println(Math.sqrt(Math.abs(c)));
        //Hypotenuse();
        Random Randinst = new Random();
        int r1 = Randinst.nextInt(7) + 1;
        double r2 = Randinst.nextDouble(); //between 0 and 1
        boolean condition = Randinst.nextBoolean();
        System.out.println(r1 + " and " + r2 + " and " + condition);
    }
}
