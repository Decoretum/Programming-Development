import java.util.*;
import java.time.*;
import java.time.format.DateTimeFormatter;

//this setup is ideal if you're working with a single file

enum Threats{
    ABYSS(500),
    FIRE(400),
    DARKNESS(300),
    COWARDICE(200);

    int Value;

    private Threats(final int value){
        this.Value = value;
    }

    public int ThreatValue(){
        return this.Value;
    }
}

interface Human {
    public void Info();
}

interface Beast {
    public void Urges();
}

class HumanBeast implements Human, Beast{
    String Name;
    String Hobbies;
    int Age;
    String Urges;
    String Bodytype;
    String Threat;

    public HumanBeast(String name, String bodytype, String hobbies, int age, String urges,String threat){
        Name = name;
        Bodytype = bodytype;
        Hobbies = hobbies;
        Age = age;
        Urges = urges;
        Threat = threat; 

    }
    public void Info(){
        System.out.printf("Name: %s, Age %d, Hobbies: %s",this.Name,this.Age,this.Hobbies);
    }
    public void Urges(){
        System.out.printf("Urges: %s, Bodytype: %s",this.Urges, this.Bodytype);
    }
    public void Threat(){
        int condition = 99;
        int loop = 0;
        int finalloop = 1;
        for (Threats threat : Threats.values()){
            while (loop == 0 && finalloop < Threats.values().length){
                if (this.Threat.toLowerCase() == threat.toString().toLowerCase()){
                    condition = 1;
                    loop = 1;
                }else{
                    condition = 0;
                }
                finalloop++;
            }
        }
            if (condition == 0){
                System.out.printf("%s does not fear the Absolutes!",this.Name);    
            }
            else{
                System.out.printf("%s fears!", this.Name);
            }
        
    }

    public void Questions(){
        Scanner question = new Scanner(System.in);
        System.out.println("");
        System.out.printf("What do you think is the right Power for you, %s?\n",this.Name);
        String choices[] = {"A: Fire Breath","B: Ice Shield","C: Battle Prowl"};
        for (int i=0;i<choices.length;i++){
            System.out.println(choices[i]);
        }
        String Choice = question.nextLine();
        if (Choice.equals("A")){
            System.out.printf("\nImpressive! Correct!");
        }
        else if (Choice.equals("B")){
            System.out.printf("\nIt could be, but not for now, %s",this.Name);
        }
        else if (Choice.equals("C")){
            System.out.printf("\nIt could be worse, but this could also suit you, %s",this.Name);
        }
        question.close();
    }
}









class ClassOne{
    int d1 = 5;
    int d2 = 10;

    void Calculate(int a, char symb, int b){
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

    public void DateNow(){
        LocalDate NowDate = LocalDate.now();
        System.out.println(NowDate);
    }

    public void TimeNow(){
        LocalTime NowTime = LocalTime.now();
        System.out.println(NowTime);
    }

    public void TimeDate(byte a){
        LocalDateTime Now = LocalDateTime.now();
        if (a == 0){
        System.out.println(Now);
    }
        else{
        DateTimeFormatter Better = DateTimeFormatter.ofPattern("MM-dd-YYYY : HH:mm:ss");
        String BetterDateTime = Now.format(Better);
        System.out.println(BetterDateTime);
        }
}
}



class ClassTwo{
    int d3 = 10;
    int d4 = 96;

    void Compare(int a, int b){
        System.out.println(a > b);
    }
    public void Describe(){
        System.out.println("This is " + d3 + " and this is " + d4);
    }


    public Object[] AddtoArray(Object array[], Object element){
        Object newarray[] = new Object[array.length + 1];

        for (int i=0; i < array.length; i++){
            newarray[i] = array[i];
        }

        newarray[array.length] = element;

        return newarray;
    }
}

public class MultipleClasses2 {
    public static void main (String args []){
        Object array[] = {1,2,3,4,5,6};
        ClassOne Test1 = new ClassOne();
        Test1.Calculate(123, '-',12321);
        Test1.DateNow();
        Test1.TimeNow();
        Test1.TimeDate((byte) 1);

        

        ClassTwo Test2 = new ClassTwo();
        Test2.Compare(12, 91);
        Test2.Describe();
        array = Test2.AddtoArray(array, 10);
        for (int i=0; i<array.length; i++){
            System.out.print(array[i] + " ");
        }
        System.out.println("");
        Object[]secondarray = Test2.AddtoArray(array, 15);
        for (int i=0; i<secondarray.length; i++){
            System.out.print(secondarray[i] + " ");
        }



        System.out.println("");
        HumanBeast Gael = new HumanBeast("Gael", "Monstrous", "Programming", 19, "Magic Practice", "Fire");
        Gael.Info();
        System.out.println("");
        Gael.Urges();
        System.out.println("");
        Gael.Threat();
        //System.out.println("");
        //Gael.Questions();

        System.out.println("");
        
        ArrayList<Object> Numbers = new ArrayList<Object>();
        Numbers.add(5);
        Numbers.add(7);
        Numbers.add(69);
        Numbers.set(0,9);
        Numbers.add("Yo");
        Numbers.add(true);
        System.out.println("");
        System.out.print(Numbers + " and" + Numbers.size() + " size");
        System.out.println(Numbers.get(3) instanceof String);
        for (int i=0; i < Numbers.size(); i++){
            System.out.println(Numbers.get(i));
        }

        //linked list



    }
}
