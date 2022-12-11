package ObjectsSystem;
import java.util.*;

public class Intro{
    private static String Name = "Gael";
    private static int Age = 19;
    private static String Specialization = "Enterprise Systems";
    private static String CareerPath = "Software Development";
    private static HashMap <Object,Object> Weapons = new HashMap<>();
    private static void Introduction(){
        System.out.println(String.format("%s is age %d. He specializes in %s for the career of %s",Name,Age,Specialization,CareerPath));
    }

    static void WeaponOfChoice(String name, String Affinity, String Purpose, String Type){
        Weapons.put("Weapon Name",name);
        Weapons.put("Weapon Affinity",Affinity);
        Weapons.put("Purpose",Purpose);
        Weapons.put("Weapon Type",Type);
        System.out.println(String.format("Weapon '%s' has been initialized.",Weapons.get("Weapon Name")));
    }

    static void ShowWeapon(){
        System.out.println(String.format("%s has a weapon named '%s' with an affinity of %s with the purpose: '%s'. It is a %s type.",Name,Weapons.get("Weapon Name"),Weapons.get("Weapon Affinity"),Weapons.get("Purpose"),Weapons.get("Weapon Type")));
    }

    static void ChangeWeapon(String Choice, String NewValue){
        Weapons.put(Choice,NewValue);

    }

    public static void main(String args[]){
        Introduction();
        WeaponOfChoice("Mystrus", "Abyssal", "Destroy/Defense", "Range");
        ShowWeapon();
        ChangeWeapon("Weapon Name", "Decoretum");
        ShowWeapon();
        ChangeWeapon("Weapon Type", "Melee");
        ShowWeapon();
    }
}