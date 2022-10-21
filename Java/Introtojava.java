public class Introtojava { //class should always start with upper letter

    static void GaelMethod(int[] array){ //static void since it doesnt return a value

        int Void = 12312; //you can declare and initialize variables within functions to be used
        for (int i1=0; i1 < array.length; i1++){
            System.out.println(array[i1]);

        };

        System.out.println("Gael has finished counting!");
        System.out.println("The sum is: wait!");
        System.out.println(Void);
    }

    static String NumberandString(String a, int b){ //static String since method should return a String 
        b += 69;
        String Statement = "String of " + a + " with a lucky number of " + b;
        return Statement;
    }

    static void ChecktheNumber(int x, String z){
        if (x >= 19 && z == "F"){
            System.out.println("You are legal. Time to pound you to pieces");
        }
        else if (x < 19 && z == "F"){
            System.out.println("I see you have a fresh pussy, cute bitch.");
        }

        if (x >= 19 && z == "M"){
            System.out.println("Time to fuck them, son.");
        }
        else if (x < 19 && z == "M"){
            System.out.println("It\'s all about the cum, son.");
        }
    }

    static void Gael(String a, int b){ //
        b += 1239;
        String A1 = "You have chosen the String of: " + a;
        String A2 = "Now, your integer is: " + b;
        System.out.println(A1 + "\n" + A2);

    }

    static void Gael(String a, float b){ //
        b += 1239;
        String A1 = "You have chosen the String of: " + a;
        String A2 = "Now, your float is: " + b;
        System.out.println(A1 + "\n" + A2);

    }

    

    public static void main(String args[]){
        
        //variables
        // must begin with letters
        String Gael = "Gael is Strong!";
        int GaelAge = 19;
        final char Code = 'G';
        float mine = 5.123124f; //add f to end of float to make it register as float, not double
        String Statement = Gael + " and is " + GaelAge + " with a code of " + Code + ".";
        boolean condition;
        condition = true;

        System.out.println("My name is Gael! First Java Program!");
        System.out.println("I want to learn how to be good at Java to potentially create applications in the future!");
        System.out.print("For Glory!"); //not a newline
        System.out.print(" For Coding knowledge!");

        //primitive data types, predefined by java
        byte x = 5; //-128 and 127
        short x1 = 123; //-32768 to 32767
        int a = 5, b = 12, y = 12121; //-2147483648 to 2147483647
        float smalldecimal = 1.212f; //6-7 decimal places, suffix of f
        double more = 5.1231231d; //15 decimal places, ends with suffix of d
        long bignum = 123123123L; //-9223372036854775808 to 9223372036854775807, ends with suffix of L
        boolean what = false;

        double A1 = 4.12e4d; //e represents power of 10
        

        char sym = '%'; //used for ASCII values
        char design = '~';


        //widening casting, narrowing casting
        short h1 = 12;
        double h2 = h1; // we changed to a larger data type

        long h3 = 12312312L;
        byte h4 = (byte) h3; // we changed to smaller data type

        System.out.println("\n");
        System.out.println(41 + 1234124);
        System.out.print(Gael + " He is " + GaelAge + " years old!");
        System.out.println("Here is a random decimal: " + mine);
        System.out.println(design + "Gael has a float of: " + mine + " with a condition of " + condition);
        System.out.println(Statement);


        //operators

        //arithmetic
        // +, -, *, /, %, ++ (increment by 1), -- (decrement by 1), % (modulo, returns division remainder)
        int samplenum = 12;
        samplenum++;
        int samplenum1 = 15;
        samplenum &= 3;
        // =, +=, -=, *=, /=, %= (modulo), 

        //comparison
        //same shit!

        // logical 
        // && returns true if both statements are true
        // || returns true if one of the statements is true
        // ! not, reverses result, returns false if result is true. Else, true

        int A0 = 123124;
        long A2 = 12312415L;
        double A3 = 121.1124d;
        boolean verdict1 = !(A0 == A2 && A3 >= A2);
        boolean verdict2 = (A2 == A3 || A3 <= A2);

        System.out.println("\n");

        System.out.println(more); 
        System.out.println(A1); 
        System.out.println(what + " "  + h2 + " " + h4 + " " + samplenum + " " + samplenum1);
        System.out.println(verdict1 + " and " + verdict2);

        //Strings and methods

        String sampletext = "What you say? Know that you only know well.";
        long length = sampletext.length(); //upper case and lowercase
        String BIG = sampletext.toUpperCase();
        String SMALL = sampletext.toLowerCase();

        int index1 = sampletext.indexOf("you"); // index
        int index2 = sampletext.indexOf("you",2);

        System.out.println(length + " and has variants of " + " " + SMALL + " " + BIG);
        System.out.println(index1 + " " + index2);

        String combined = sampletext.concat("Fuck me!"); //concatenate haha
        System.out.println(combined);

        //numbers and strings
        String hybrid = A0 + Gael;
        System.out.println(hybrid); //string + number = string concatenation

        //special characters, use \ before \,', "
        // \n for newline, \r carriage return (similar to newline), \t tab, \b backspace, \f form feed
        String special = "This is Gael\'s \nspeciality!";
        System.out.println(special);

        //Java math class
        System.out.println("");
        System.out.println(Math.max(1,45));
        System.out.println(Math.min(1,2));
        System.out.println(Math.sqrt(1294));
        System.out.println(Math.abs(-124.91));
        double random = (double)(Math.random() * 101);
        System.out.println(random);

        //Boolean expression
        System.out.println(12312 > 22222);
        System.out.println(bignum <= more);
        System.out.println("");

        //conditional if else statements
        if ( !(bignum >= more) || 3 > 2 ){
        System.out.println("Results are cool!");
        };

        if (!(5 < 3)){
        System.out.println("Lol");
        };

        int conditionresult = (124 > 12) ? 69 : 1000; //shorthand if else
        System.out.println(conditionresult);
        System.out.println("");

        //java switch elements

        String GaelCondition = "I dont know how i feel";
        switch(GaelCondition){
            case "Gael feels very relaxed!":
                System.out.println("Oh yeah baby! He is feeling great!");
                break;
            case "Gael feels shitty":
                System.out.println("What the fuck man...");
                break;
            case "Mad motherfucker":
                GaelCondition = "Gael is here now...";
                System.out.println(GaelCondition);
                break;
            default:
                System.out.println("Gael is a robot!");
                break;
        }

        //java while loop and do/while 
        long straightup = 500;
        while(straightup > 100){
            System.out.println(straightup);
            straightup -= 100;
        };


        //do block is executed once no matter condition then checks condition
        int NumberCool = 19201;
        do {
            NumberCool -= 19201;
            System.out.println("No way, Jose!");

        }
        while(NumberCool == 19201);

        System.out.println("");

        int i = 0;
        while (i < 5){
            System.out.println(i);
            i++;
        };

        System.out.println("");

        if (!(i < 5)){
            System.out.println(i);
        }

        System.out.println("");

        //for loop

        for(int i1 =0; i1 <10; i1+=2,System.out.println("Increased!")) { //executed one time; conditions for executing loop; what to execute once code block is executed;
        System.out.println(i1);

        };

        System.out.println("");

        //non-primitive data types, created by programmer
        //arrays
        String[] Array1 = {"Gael", "Iris", "Tini", "Tita Jan", "Lola Nene"};
        System.out.println(Array1);

        for (int i1=0; i1<Array1.length; i1++){
            System.out.println("Name: " + Array1[i1]);

        };

        System.out.println("");

        //for each loop

        for(String i1 : Array1){
            System.out.println(i1);
        }

        //multidimensional arrays
        //array/s within an array

        System.out.println("");
        int[][] array2 = {{1,2,3,4,1,21,1231,51,75},{2,4,12,521,8562}};
        System.out.println(array2[0][0]);

        for(int i1=0; i1 < array2.length; i1++){
            for (int i2=0; i2 < array2[i1].length; i2++ ){
                System.out.println(array2[i1][i2]);
            }
        }

        System.out.println("");
        int[][][] array3 = { {{1,2,3,4,5},{6,7,8,9,10}} , {{11,12,13,14},{15,16,17,18}} };

        for (int i1=0; i1 < array3.length; i1++){ //iterates over 2ndmost array
            for (int i2 = 0; i2 < array3[i1].length; i2++){ //iterates over 3rdmost arrays
                for (int i3=0; i3 < array3[i1][i2].length; i3++){
                    System.out.println(array3[i1][i2][i3]);
                }
            }
        }

        System.out.println("");

        //result of function
        int [] array4 = {1,2,3,4,5,6,7};
        GaelMethod(array4);
        System.out.println(NumberandString("Justin",69)); //console log since returns a value

        System.out.println("");

        String GaelTurn = NumberandString("Gael",19);
        String Justin = "suckmacock";
        System.out.println(Gael.equals(Justin));
        System.out.println(GaelTurn);

        System.out.println("");

        ChecktheNumber(19,"M");

        System.out.println("");

        ChecktheNumber(17, "F");

        System.out.println("");

        Gael("Love",50); //same method names but different methods due to parameters
        Gael("Arrogance",120.1212f); 

        System.out.println("");

        


        














    }

    
    };

