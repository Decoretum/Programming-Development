package LearnJava;

import java.util.ArrayList;

public class Weapon {
    String Affinity;
    String name;
    static ArrayList <String> Weapons = new ArrayList<>();
    Weapon(String name,String Aff){
        this.name = name;
        this.Affinity = Aff;
        Weapons.add(String.format("%s with the affinity of %s",this.name,this.Affinity));
    }

    String Name(){
        return this.name;
    }
}
