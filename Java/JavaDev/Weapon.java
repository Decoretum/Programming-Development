package JavaDev;

import java.util.ArrayList;

public class Weapon {
    String Affinity;
    String name;
    static ArrayList <String> Weapons = new ArrayList<>();
    public Weapon(String name,String Aff){
        this.name = name;
        this.Affinity = Aff;
        Weapons.add(String.format("%s with the affinity of %s",this.name,this.Affinity));
    }

    public void WeaponList(){
        for (String i : Weapons){
            System.out.println(i);
        }
    }

    String Name(){
        return this.name;
    }
}
