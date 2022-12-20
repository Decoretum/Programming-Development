package LearnJava;

public class Magi {
    String name;
    String Specialization;
    String Aura;
    int Age;
    Weapon Weapon;

    Magi(String name, String spec, String aura, int age, Weapon wep){
        this.name = name;
        this.Specialization = spec;
        this.Aura = aura;
        this.Age = age;
        this.Weapon = wep;
        System.out.println(String.format("Magi %s has been initiated into this world.",this.name));
    }

    void BattleCry(){
        System.out.println(String.format("I, %s, shall devour you with my %s",this.name,this.Specialization));
    }

    void PrepWep(){
        System.out.println(String.format("%s has charged his weapon '%s' with his power of %s!",this.name,this.Aura,this.Weapon.Name()));
    }
}
