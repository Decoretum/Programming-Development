package JavaDev;

public class Apprentice extends Magi{
    String University;
    public Apprentice(String name, String spec, String aura, int age, String University){
        super(name,spec,aura,age);
        this.University = University;
    }

    public void BattleCry(){
        super.BattleCry();
        System.out.println("I'll eventually be a Magi after I have defeated you!");
    }

}   
