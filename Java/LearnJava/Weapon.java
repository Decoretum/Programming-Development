package LearnJava;

public class Weapon {
    String Affinity;
    String name;
    Weapon(String name,String Aff){
        this.name = name;
        this.Affinity = Aff;
    }

    String Name(){
        return this.name;
    }
}
