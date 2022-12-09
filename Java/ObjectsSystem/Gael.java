//This java file simulates a software engineer / developer's life 
package ObjectsSystem;
import java.util.*;
import java.io.*;

public class Gael{
    private String Specialization = "Programming";
    private String Fear = "Insects";
    String Interests = "Programming, Video Games, Music, Pewdiepie";
    short Age = 19;
    char Gender = 'M';
    private int Money;
    private String Agenda = "";
    private String Condition = "Neutral";
    private String Name;
    private int NoteCount = 0;


    public Gael(String name){
        Name = name;
        Money = 0;
        System.out.println(String.format("%s has been born! Time to live a new life.",Name));
        Mission();
    }

    public void MyName(){
        System.out.println(String.format("My name is %s.",Name));
        Mission();
    }
    
    public void Savings(){
        System.out.println(String.format("Current Money: %d Pesos",Money));
    }

    public void ManAge(){
        System.out.println(String.format("Age: %d",Age));
        Mission();
    }

    public void EarnMoney(){
        System.out.println(String.format("%s will now be earning Money",Name));
        if (Money < 1000){
            int earn1 = 100;
            Money += earn1;
            System.out.println(String.format("%s has earned %d",Name,earn1));
            if (Money >= 1000){
                System.out.println(String.format("%s has finally reached 1000 Pesos!",Name));
            }
        }

        else if (Money >= 1000){
            int earn1 = 200;
            Money += earn1;
            System.out.println(String.format("%s has earned %d",Name,earn1));
        }
        
    }

    public void Mission(){ 
        System.out.println("");
        System.out.println("So much options in life! What to do?:\na. Work\nb. Study\nc. Watch Youtube/Netflix\nd. Gamble\n e. Rest\nf. Note-Taking");
        Scanner line = new Scanner(System.in);
        String choice = line.next();
        if (choice.equals("a")){
            Work();
        }
        else if (choice.equals("b")){
            System.out.println("Time to study and do your work!");
           
            //Direct to work method
        }
        else if (choice.equals("c")){
            System.out.println("Time to Relax and Chill!");
           
            //Direct to relax method
        }
        else if (choice.equals("d")){
            System.out.println("Time to Gamble, oh no....");
            
            Gamble();
        }
        else if (choice.equals("e")){
            Rest();
        }
        else if (choice.equals("f")){
            InfiniteInput();
        }

    }


    public void Feel(){
        System.out.println("");
        System.out.println(String.format("%s feels %s right now.",Name,Condition));

    }

    public void Work(){
        System.out.println("");
        Scanner input = new Scanner(System.in);
        int luck = (int) ((Math.random() * (4-1)) + 1);
        if (luck == 1){
            System.out.println("Your project manager fucked your code up! What do you do?");
            String choices = "a. Fix your code yourself and report your manager!\nb. Report it to your senior software engineer!\nc. Post that on r/programmerhumor in reddit";
            System.out.println(choices);
            String choice1 = input.next();
            if (choice1.equals("a")){
                
                System.out.println("Wonderful! Your project manager will be fired, and you will be paid!");
                EarnMoney();
            }
            else if (choice1.equals("b")){
                
                System.out.println("Your senior software engineer will thank you for being transparent. You will be paid!");
                EarnMoney();
            }
            else if (choice1.equals("c")){
                
                System.out.println("You will become a sensation and an inspiration for many programmers all around the world!");
                Condition = "Happy";

            }
         
        }
        else if (luck == 2){
            System.out.println("Your management fucks up your programming methodology! What do you do?");
            String choices = "a. Report it straight to HR!\nb. Report it to your senior software engineer!\nc. Rant to your chief executive officers!";
            System.out.println(choices);
            String choice2 = input.next();
            if (choice2.equals("a")){
               
                System.out.println("HR acknowledges your concerns. Management will be reprimanded and fucked! You don't get paid too....");
                Condition = "Happy";
            }
            else if (choice2.equals("b")){
                
                System.out.println("Your senior software engineer will suffer alongside you, and you will get paid");
                Condition = "Sad";
                EarnMoney();
            }
            else if (choice2.equals("c")){
               
                System.out.println("Your chief executive officers will laugh at you and will decrease your wage!");
                Condition = "Sad";
                
            }

        }
        else if (luck == 3){
            System.out.println("Someone forced commit an unwanted pull request to the repository, what do you do?");
            String choices = "a. Threaten that fucker with all your might\nb. Remove access and view of your repository to that programmer\nc. Tell your senior to fire him/her";
            System.out.println(choices);
            String choice3 = input.next();
            if (choice3.equals("a")){
                
                System.out.println("The fucker will not bother your code, your repository, and even the web frameworks that you use! Fucker is finished! You don't get paid though");
                Condition = "Happy";
            }
            else if (choice3.equals("b")){
               
                System.out.println("The fucker will continue finding ways to make those pull requests, but he/she is finished for now...");
                Condition = "Happy";
                EarnMoney();
            }
            else if (choice3.equals("c")){
               
                System.out.println("The programmer for that pull request was fired, and you gazed into his/her eyes with pride!");
                Condition = "Happy";
                EarnMoney();
            }
        
        }
        Feel();
        Savings();
        Mission();
    }

    public void Gamble(){
        System.out.println("");
        double maximum = 0;
        ArrayList<Double> guesses = new ArrayList<>();
        int luck = (int) ((Math.random() * (3-1)) + 1);
        
        for (int i=0; i<4;i++){
            double guess = Math.floor(Math.random()*100);
            guesses.add(i, guess);
        }

        for (int i=0;i<guesses.size();i++){
            maximum = guesses.get(i);
            if(guesses.indexOf(guesses.get(i)) == guesses.size()-1){
                System.out.println(guesses.get(i) + " END");
            }
            else{
                System.out.print(guesses.get(i) + "->");
            }
            if (maximum < guesses.get(i)){
                maximum = guesses.get(i);
            }
        }

        if (luck == 1){
            Money -= maximum;
            System.out.println(String.format("You lost %s",maximum));
        }
        else if (luck == 2){
            Money += maximum;
            System.out.println(String.format("You won %s",maximum));
        }
        
        Savings();
        Mission();
    
    }

    public void Rest(){
        System.out.println(String.format("You have done well, %s",Name));
        System.out.println(String.format("It is time for you to rest!"));
        System.out.println(String.format("Money: %d \nCondition: %s\n",Money,Condition));
        System.out.println("Check the directory for the stats of your performance");
        try{
            FileWriter rawstats = new FileWriter("../PersonalProjects/Java/ObjectsSystem/GaelSystem.txt");
            BufferedWriter Stats = new BufferedWriter(rawstats);
            Stats.write("| GAEL SYSTEM STATS PERFORMANCE |");
            Stats.newLine();
            Stats.write(String.format("| NAME | --> %s",Name));
            Stats.newLine();
            Stats.write(String.format("| CONDITION | --> %s",Condition));
            Stats.newLine();
            Stats.write(String.format("| AGE | --> %s",Age));
            Stats.newLine();
            Stats.write(String.format("| CURRENT CONDITION | --> %s",Condition));
            Stats.newLine();
            Stats.write(String.format("| MONEY | --> %d",Money));
            Stats.flush();
            Stats.close();
        }
        catch (IOException e){
            System.out.println("Error with Gael System occurred");
            e.printStackTrace();
        }
    
    }
    
    public void InfiniteInput(){
        ArrayList<Object> NoteArray = new ArrayList<>(); 
        System.out.println("You will start writing your own Notes as of now! Prepare the lines");
        System.out.println(String.format("%s's Notes",Name));    
        Scanner LineNotes = new Scanner(System.in);
        try{
            FileWriter raw = new FileWriter(String.format("../PersonalProjects/Java/ObjectsSystem/%sNotes%d.txt",Name,NoteCount));
            BufferedWriter notes = new BufferedWriter(raw);
            while(true){
                String newnotes = LineNotes.nextLine();
                if (newnotes.equals("DONE")){
                    System.out.println("You have finally finished Note-taking!");
                    for (int i=0;i<NoteArray.size();i++){
                        notes.write(String.format("Entry %d: ",i+1));
                        notes.write(NoteArray.get(i).toString());
                        notes.newLine();
                    }
                    notes.flush();
                    notes.close();
                    raw.close();
                    NoteCount++;
                    for (Object i : NoteArray){
                        System.out.println(i);
                    }
                    break;
                }  
                else{
                    NoteArray.add(newnotes);     
                }
        }
            Mission();
        }
        catch (IOException e){
            System.out.println("Error");
            e.printStackTrace();
        }
    }

}