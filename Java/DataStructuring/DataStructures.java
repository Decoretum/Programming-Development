package DataStructuring;
import java.util.*;

public class DataStructures {

    
    public static void main (String args[]){

        ArrayList<Integer> Num = new ArrayList<Integer>();
        Num.add(5);
        Num.add(2);
        Num.add(1);
        Collections.sort(Num);
        System.out.println(Num);

        //remember your algorithms class
        //similar to arraylists in java
        LinkedList<String> Characters = new LinkedList<String>();
        Characters.add("Gael");
        Characters.add("Angela");
        Characters.add("Jam");
        Characters.removeLast();
        Characters.addLast("Joe");
        Characters.set(1,"Lia");
        Collections.sort(Characters);
        System.out.println(Characters);
        System.out.println(Characters.getLast());
        

        //Hashmap
        HashMap<Integer,String> Projects = new HashMap<Integer,String>();
        Projects.put(0,"Java");
        Projects.put(1,"Web Development");
        Projects.put(2,"JavaScript");
        System.out.println(Projects);
        System.out.println(Projects.get(1));

        HashMap<String,Integer> Adventures = new HashMap<String,Integer>();
        Adventures.put("Matilda",69);
        Adventures.put("Ramsay", 9);
        Adventures.put("Lala", 99);

        //loop through keys using .keySet() and values using .values() or size()
        for (int i=0; i<Projects.size(); i++){
            System.out.println(Projects.get(i));
        }

        for (int i : Projects.keySet()){
            System.out.println(i + " and " + Projects.get(i));
        }

        for (String i : Adventures.keySet()){
            System.out.printf("%s with the value of %d\n", i, Adventures.get(i));
        }

        int loop = 0;
        int end = 1;
        
        
        Scanner projects = new Scanner(System.in);
        System.out.println("What do you want to focus on?");
        String answer1 = projects.nextLine();
        while (loop == 0 && end < Projects.keySet().toArray().length){
            for (int i : Projects.keySet()){
            if (Projects.get(i).equals(answer1)){
                System.out.println("It's what you are doing now!");
                loop = 1;
            }
            end++;
        }
    }

        if (loop == 1){
            Scanner Congrats = new Scanner(System.in);
            System.out.println("What can you say, Java bro?");
            String answer = Congrats.nextLine();
            System.out.println("Answer of Java boy: " + answer);
            Congrats.close();
        }
        else if(end > Projects.keySet().toArray().length){
            System.out.println("You do not align with us");
        }

        projects.close();
        



    }
}
