package ObjectsSystem;
import java.util.*;

public class Intro{
    static String Name = "Gael";
    static int Age = 19;
    static String Specialization = "Enterprise Systems";
    static String CareerPath = "Software Development";
    static HashMap <Object,Object> Weapons = new HashMap<>();
    static void Introduction(){
        System.out.println(String.format("%s is age %d. He specializes in %s for the career of %s",Name,Age,Specialization,CareerPath));
    }

    static void WeaponOfChoice(String name, String Affinity, String Purpose, String Type){
        Weapons.put("Weapon Name",name);
        Weapons.put("Weapon Affinity",Affinity);
        Weapons.put("Purpose",Purpose);
        Weapons.put("Weapon Type",Type);
    }

    public static void main(String args[]){
        Introduction();
        
    }
}