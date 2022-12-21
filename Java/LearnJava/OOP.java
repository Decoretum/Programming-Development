package LearnJava;
import java.util.*;

public class OOP {
    public static void main (String args[]){
        Weapon ChaosStaff = new Weapon("Staff of Chaos","Abyss");
        Magi Gael = new Magi("Gael", "Destruction & Alteration", "Abyss", 19);
        Magi Solomon = new Magi("Solomon", "Alteration & Restoration", "Light", 14, "Linda's Light");
        Magi Sinbad = new Magi("Sinbad","Destruction","Lightning",20,"Belark's Thunder");
        System.out.println(Sinbad.Weapon.Affinity);
        Object[] Magis = new Object[3];
        ArrayList<Object> Magises = new ArrayList<>();
        Magis[0] = Gael;
        Magis[1] = Solomon;
        Magis[2] = Sinbad;
        for (int i = 0; i < Magis.length; i++){
            System.out.println(Magis[i]);
        }



    }
    

}
