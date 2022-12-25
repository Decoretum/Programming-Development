package JavaDev;

import java.util.ArrayList;

public class Magi {
    Weapon Weapon;
    String name;
    String Specialization;
    String Aura;
    byte Charge = 0;
    int Age;
    static ArrayList <Magi> MagisAura = new ArrayList<>(); //this is a single variable shared among all object instances since its on one class

    Magi(String name, String spec, String aura, int age){
        this.name = name;
        this.Specialization = spec;
        this.Aura = aura;
        this.Age = age;
        MagisAura.add(this);
        System.out.println(String.format("Magi %s has been initiated into this world.",this.name));
    }

    Magi(String name, String spec, String aura, int age, String Weapon){
        this.Weapon = new Weapon(Weapon, aura);
        this.name = name;
        this.Specialization = spec;
        this.Aura = aura;
        this.Age = age;
        MagisAura.add(this);
        System.out.println(String.format("Magi %s has been initiated into this world with the weapon '%s' of the %s.",this.name,this.Weapon.Name(),this.Weapon.Affinity));
    }

    public String toString(){ //implicit and explicit return when calling an object
        return "(Magi Name: " + this.name + " || Magi Age: "  + this.Age + " || Magi Specialization: " + this.Specialization + " || Magi Aura: " + this.Aura + ")";
    }

    void TakeWeapon(Weapon wep){
        this.Weapon = wep;
        System.out.println(String.format("The weapon '%s' has been acquired by %s.",this.Weapon.Name(),this.name));
    }
    void BattleCry(){
        System.out.println(String.format("I, %s, shall devour you with my %s",this.name,this.Specialization));
    }

    void PrepWep(){
        if (this.Weapon != null){
            System.out.println(String.format("%s has charged his weapon '%s' with his power of %s!",this.name,this.Aura,this.Weapon.Name()));
            this.Charge = 1;
        }
        else{
            System.out.println(String.format("%s currently has no weapon equipped, cannot prepare null weapon.",this.name));  
        }
        
    }

    void Attack(){
        if (this.Weapon != null){
            if (this.Charge == 1){
                System.out.println(String.format("%s launches %s bolts with the %s!",this.name,this.Aura,this.Weapon.Name()));
            }
            else{
                System.out.println(String.format("The %s has not been charged yet.",this.Weapon.Name()));
            }
        }
        else{
            System.out.println(String.format("%s currently has no weapon equipped, cannot attack.",this.name));
        }
        
    }   
    
}
