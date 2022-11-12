//This setup is ideal if you want to import these classes of the public class to another file

public class MultipleClasses { //several classes enclosed in one public class, useful for importing the enclosed classes to another file
    public void Compare3(int a, int b){
        System.out.println(a < b);
    }


    public class ClassOne{
        int d1 = 5;
        int d2 = 10;

        public void Calculate(int a, char symb, int b){
            int result = 0;
            if (symb == '+'){
                result = a + b;
            }
            else if (symb == '-'){
                result = a - b;
            }
            else if (symb == '*'){
                result = a * b;
            }
            else if (symb == '/'){
                result = a / b;
            }
            System.out.println(result);
        }
    }



        public class ClassTwo{
        int d3 = 10;
        int d4 = 96;

         void Compare(int a, int b){
            System.out.println(a > b);
        }
        static void Compare2(int a, int b){
            System.out.println(a > b);
        }
        public void Describe(){
            System.out.println("This is " + d3 + " and this is " + d4);
        }

        public static void main (String args[]){
            System.out.println("Can you hear me?");
        }
    }

        public class ClassThree{
            int a = 123;
            int b = 12;
             void Greet(){
                System.out.println("Yo!");
            }
        }
        


    public static void main (String args []){
        MultipleClasses t1 = new MultipleClasses(); //instantiate main class
        ClassOne Test1 = t1.new ClassOne();
        Test1.Calculate(123, '-',12321);
    

        ClassTwo Test2 = t1.new ClassTwo();
        Test2.Compare(12, 91);
        Test2.Describe();

        
    }
}
