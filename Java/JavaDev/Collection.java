package JavaDev;
import java.util.*;;

public class Collection {

    public static void main (String args[]){
        ArrayList <String> Hobbies = new ArrayList<>();
        Hobbies.add("Speedcubing");
        Hobbies.add("Programming");
        Hobbies.add("Gaming");

        ArrayList <String> Specialization = new ArrayList<>();
        Specialization.add("Software Development");
        Specialization.add("Database Querying");
        Specialization.add("Web Development");

        ArrayList <String> Personality = new ArrayList<>();
        Personality.add("Humble");
        Personality.add("Charming");
        Personality.add("Charistmatic");
        Personality.add("Brave");

        ArrayList <ArrayList<String>> Characteristic = new ArrayList<>();
        Characteristic.add(Hobbies);
        Characteristic.add(Specialization);
        Characteristic.add(Personality);

        for (int i=0; i<Characteristic.size();i++){
            System.out.println("Index " + Characteristic.indexOf(Characteristic.get(i)) + ": " + Characteristic.get(i));
        }

        System.out.println(Characteristic.get(0).get(2));

        for (int i = 0; i < Characteristic.size(); i++){
            System.out.println(Characteristic.get(i).get(0));
        }





    }
}
