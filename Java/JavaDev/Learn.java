package JavaDev;

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
        String word = input.nextLine();
        while (word.isBlank()){
            word = input.nextLine();
        }
        if (word.equals("Done")){
            System.out.println("Chill, you're done now");
        }
        else{
            System.out.println("Loop done");
        }
        
        input.close();

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

    static void Matrix(int rows, int columns){
       for (int i=0;i <= rows-1;i++){
            System.out.println();
            for (int j=0; j <= columns-1; j++){
                System.out.print(" 0 ");
            }
       }
        
    }

    static void Matrix2d(int rows, int columns){
        Object[][] matrix = new Object[rows][columns];
        for (int i = 0; i <= matrix.length - 1; i++){
            System.out.println();
            for (int j = 0; j <= matrix[i].length - 1; j++){
                matrix[i][j] = j+1;
            }
        }
        matrix[2][2] = "!";

        for (int i = 0; i <= matrix.length - 1; i++){
            System.out.println();
            for (int j = 0; j <= matrix[i].length - 1; j++){
                System.out.print(matrix[i][j] + " ");
            }
        }
    }
        
    
    static void AddtoArray(Object[] array,Object element){
        Object[] NewArray = new Object[array.length + 1];
        for (int i=0; i<=array.length-1; i++){
            NewArray[i] = array[i];
        }
        NewArray[NewArray.length - 1] = element;
        for (int i = 0; i<= NewArray.length; i++){
            System.out.print(NewArray[i] + " ");
        }
    }

    public static void main (String args[]){
        Object[] CoolArray = {1,2,3,4,5,6,7};
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
        //Playtime();
        //Matrix(5, 5);
        //AddtoArray(CoolArray, "infinity");
        System.out.println("\n");
        Matrix2d(6, 6);
    }
}
