package DataStructuring;
import java.util.*;

public class DataStructures2 {
    static void Identity(ArrayList<Object>array){
        ArrayList<Object>Getter = new ArrayList<Object>();
        for (int i=0;i<array.size();i++){
            if (array.get(i).equals("Gael") || array.get(i).equals("Decoretum")){
                Getter.add(array.get(i));
            }
        }
        System.out.println("Identities:");
        for (int i=0; i<Getter.size();i++){
            System.out.println(Getter.get(i));
        }
    }

    public void ObjectFilter(HashMap<Object,Object>Hash){
        ArrayList<Object> Errors = new ArrayList<Object>();
        for (Object i : Hash.keySet()){ //adding warnings per iteration
            if (i.equals(false)){
                Errors.add(Hash.get(i).toString());
                Hash.replace(i, Hash.get(i), "This is a fake!");
            }
        }
        if (Hash.containsValue("This is a fake!")){
            Hash.put("Authenticity",0);
        }
        for (int i =0; i<Errors.size(); i++){
            Hash.put("ERROR #" + (i+1),Errors.get(i));
        } 
        for (Object i : Hash.keySet()){
            System.out.println("Key: " + i + ". Value: " + Hash.get(i));
        }
    }

    public static void main (String args[]){
        ArrayList<Object> Normal = new ArrayList<Object>();
        Normal.add(901);
        Normal.add("Gael");
        Normal.add("Decoretum");
        Normal.add(3,9712);
        for (int i=0;i<Normal.size();i++){
            System.out.println("Position " + i + ":" + " " + Normal.get(i));
        }

        Identity(Normal);

        //hashset, Arraylist but with no duplicates
        HashSet<Object>Activities = new HashSet<Object>();
        Activities.add("Trome");
        Activities.add("Tera");
        Activities.add("Liese");
        Activities.add("Sex");
        Activities.add("Sex"); //duplicate
        for (Object a : Activities){
            System.out.println(a);
        }
        System.out.println("");

        Iterator<Object> ActIt = Activities.iterator(); //this is an object

        while(ActIt.hasNext()){ 
            System.out.println(ActIt.next()); //we return an obejct here
        }

        System.out.println(Activities);

        //using simple Java array
        Object[] SimpleArray = {"Yo",123,"Yes"};
        for (int i =0; i<SimpleArray.length;i++){
            System.out.println(SimpleArray[i]);
        }

        System.out.println("");

        HashMap<Object,Object> Achievements = new HashMap<Object,Object>();
        Achievements.put(123, "Website");
        Achievements.put("Cool","Application");
        Achievements.put(true, "Web System");
        Achievements.put(false, "Made an IOS APP");

        ArrayList<Object> Errors = new ArrayList<Object>();
        for (Object i : Achievements.keySet()){ //adding warnings per iteration
            System.out.println("Key: " + i + ". Value: " + Achievements.get(i));
            if (i.equals(false)){
                Achievements.replace(i, Achievements.get(i), "This is a fake!");
                Errors.add(Achievements.get(i).toString());
            }
        }

        System.out.println("");

        for (int i =0; i<Errors.size(); i++){
            Achievements.put("ERROR #" + (i+1),Errors.get(i));
        }

        System.out.println("");
        
        for (Object i : Achievements.keySet()){
            System.out.println("Key: " + i + ". Value: " + Achievements.get(i));
        }

        System.out.println("\n\n");

        //Iterators

        ArrayList<Object>Favourites = new ArrayList<Object>();
        ArrayList<Object>BestofFav = new ArrayList<Object>();
        Favourites.add("Food");
        Favourites.add(69);
        Favourites.add("Music");
        Favourites.add("Sandbox games");
        Iterator<Object>Fav = Favourites.iterator();
        while (Fav.hasNext()){
            Object object = Fav.next();
            if (!object.equals(69)){
                BestofFav.add(object);
            }
            System.out.println(object);
           
        }

        System.out.println("");
        
        for (Object a : BestofFav){
            System.out.println(a);
        }

        /* Trying to remove items using a for loop or a for-each loop would not work correctly 
        because the collection is changing size at the same time that the code is trying to loop. */

        System.out.println("\n\n\n");


        //Filtering stuff through HashSet
        HashSet<Object>Filter = new HashSet<Object>();
        HashSet<Object>IntFilter = new HashSet<Object>();
        HashSet<Object>BadFilter = new HashSet<Object>();
        Filter.add("Yo mama");
        Filter.add(123);
        Filter.add(1391);
        Filter.add("Gael");
        Filter.add("Hahaha lol");
        Filter.add("Fuck");
        Iterator<Object>Ft = Filter.iterator();
        while (Ft.hasNext()){
            Object ft = Ft.next();
            System.out.println(ft);
            if (ft instanceof Number){ //instanceof very important, instance of data type
                IntFilter.add(ft);
            }
            else if (ft.equals("Yo mama") || ft.equals("Hahaha lol")){
                BadFilter.add(ft);
            }
            else if (ft.equals("Fuck")){
                Ft.remove();
            }
        }

        System.out.println("\nIntegers");
        for (Object a : IntFilter){
            System.out.println(a);
        }

        System.out.println("\nBad Words");
            for (Object a : BadFilter){
                System.out.println(a);
            }
        
        System.out.println("");
        for (Object a : Filter){
            System.out.println(a);
        }

        System.out.println("\n\n\n");

        //wrapper classes allow primitive data types to be objects
        Long Name = 641212L;
        String addons = "Power Level";
        String FinalName = Name.toString() + " " + addons;
        System.out.println(Name.longValue());
        System.out.println(FinalName);

        System.out.println("\n\n");
        //try and catch
        try{
            int[] myNumbers = {1, 2, 3};
            System.out.println(myNumbers[10]);
        }
        catch(Exception e){
            System.out.println("Might be some errors, Bro");
        }
        finally{
            System.out.println("Finalizations complete");
        }

        //throwing Exceptions: ArithmeticException, FileNotFoundException, ArrayIndexOutOfBoundsException, SecurityException
        if(123 > 12){
            throw new SecurityException("The Number is not proper and appropriate!");
        }
        else{
            System.out.println("It's alright!");
        }
    }
}
