package JavaDev;

import javax.swing.*;
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

    static void Chemistry(){
        System.out.println("So, what do you want to check compatibility with?");
        System.out.println("Option 1:");
        Scanner scanner = new Scanner(System.in);
        String one = scanner.nextLine();

        System.out.println("Option 2:");
        String two = scanner.nextLine();

        if (one.equals("Good") && two.equals("Bad")){
            System.out.println("This is not compatible!");
        }

        else{
            System.out.println("This will require further assessment");
        }
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
                if (i == 2 && j == 2){
                    matrix[i][j] = "!";
                    System.out.print(matrix[i][j] + " ");
                }
                else{
                    matrix[i][j] = j+1;
                    System.out.print(matrix[i][j] + " ");
                }
            }
        }
        System.out.println();
    }

    static void MarkMatrix2d(Object[][] matrix,int x, int y, Object value){
        matrix[x][y] = value;
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

    static void NameInput(){
        Scanner scan = new Scanner(System.in);
        System.out.println("What\'s your name?");
        String name = scan.nextLine();
        if (name.equals("Gael")){
            System.out.println("Gael, you have returned!");
        }
        else{
            System.out.println("Authentication failed");
        }
    }

    static void Student(){
        String name = JOptionPane.showInputDialog("What is your name?");
        String course = JOptionPane.showInputDialog("What course do you belong to?");
        String specialization = JOptionPane.showInputDialog("Do you have any specialization?");
        int level = Integer.parseInt(JOptionPane.showInputDialog("What year level are you?"));
        String aspiration = JOptionPane.showInputDialog("What career do you want to have in the future?");
        
        if (course.equals("") || course.isEmpty()){
            JOptionPane.showMessageDialog(null, "How can you have no course? Answer it again");
        }
        else{
            if (specialization.trim().isEmpty()){
                JOptionPane.showMessageDialog(null, String.format("Student Name: %s || Student Course: %s || Year Level: %d || Aspiration: %s",name,course,level,aspiration));
            }
            else{
                JOptionPane.showMessageDialog(null, String.format("Student Name: %s || Student Course: %s || Specialization: %s|| Year Level: %d || Aspiration: %s",name,course, specialization,level,aspiration));
            }
            
        }

        System.out.println("Thank you for the input.");
        
        
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
        //Chemistry();
        //Student();
        //NameInput();
        String rand = "           ";
        String regex = "MoNsTEr";
        System.out.println(rand.trim().length());
        System.out.println("monster".contains(regex.toLowerCase()));
    }
}
