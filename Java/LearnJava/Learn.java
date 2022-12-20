package LearnJava;

import java.util.*;
public class Learn {
    //Primitive (stores data, can hold 1 value) 
    //Reference (User defined, stores address)
    static String Name = "Gael";
    static String University = "Ateneo de Manila University";
    static long Power = 9019231290123L;

    static byte Good = 4;
    static byte Bad = 10;
    static byte placeholder;
    static int Num = 15;

    static void UserInput(String User){
        Scanner Input =  new Scanner(System.in);


        System.out.println("What is your IQ?");
        int IQ = Input.nextInt();
        Input.nextLine();

        System.out.println("What do you desire, " + User + "?");
        String Desire = Input.nextLine();

        if (Desire.equals("Love")){
            System.out.println(String.format("That is a noble emotion to feel, %s",User));
        }
        else{
            System.out.println(String.format("I see, so %s is your desire, %s",Desire,User));
        }
        System.out.println(String.format("%s has an IQ of %d",User, IQ));
    }

    static void Check(int value){
        switch(value){
            default:
            System.out.println("No matches.");
            break;
            case 9:
            System.out.println("9!");
            break;
            case 5:
            System.out.println("5!");
        }
    }

    static void Playtime(){
        Scanner input = new Scanner(System.in);
        
    }

    static void Comparison(){
        Scanner input = new Scanner(System.in);
        System.out.println("What is your Power?");
        int power = input.nextInt();
        input.nextLine();
        System.out.println("What is your Age?");
        int age = input.nextInt();
        if (power > 50 && age < 15){
            System.out.println("You are talented!");
        }
        else if (power < 50 && age > 15){
            System.out.println("You suck lol");
        }
        else{
            System.out.println("No special case");   
        }
        input.close();

    }

    public static void main (String args[]){
        Num = (int) Num / 2;
        placeholder = Good;
        Good = Bad;
        Bad = placeholder;
        System.out.println("The name of the owner of this program is " + Name);
        System.out.println(Good + " and " + Bad);
        System.out.println(Num);
        //UserInput("Gael");
        //Check(100);
        //Comparison();
    }
}
