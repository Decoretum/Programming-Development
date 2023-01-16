package JavaDev;
import java.util.*;

import javax.crypto.spec.DESKeySpec;

import JavaDev.SturdyPackage.CreationAgent;
import JavaDev.SturdyPackage.Destruction;

public class OOP {
    public static void main (String args[]){
        Weapon ChaosStaff = new Weapon("Staff of Chaos","Abyss");
        Magi Gael = new Magi("Gael", "Destruction & Alteration", "Abyss", 19);
        Magi Solomon = new Magi("Solomon", "Alteration & Restoration", "Light", 14, "Linda's Light");
        Magi Sinbad = new Magi("Sinbad","Destruction","Lightning",20,"Belark's Thunder");
        System.out.println(Sinbad.Weapon.Affinity);
        Magi[] Magis = new Magi[3];
        ArrayList<Magi> Magises = new ArrayList<>();
        Magises.add(Gael);
        Magises.add(Solomon);
        Magises.add(Sinbad);
        Magis[0] = Gael;
        Magis[1] = Solomon;
        Magis[2] = Sinbad;
        for (int i = 0; i < Magis.length; i++){
            System.out.println(Magis[i].name);
        }

        for (int i = 0; i < Magises.size(); i++){
            System.out.println(Magises.get(i).name);
        }
        ArrayList <Object> Artifacts = new ArrayList<>();
        Artifacts.add(Gael);
        Artifacts.add("ME");
        Artifacts.add(12);
        System.out.println(Artifacts);
        System.out.println(Magis[0]);
        System.out.println(Artifacts.get(2));
        for (int i =0; i < Magi.MagisAura.size(); i++){
            System.out.println(Magi.MagisAura.get(i));
        }
        System.out.println(Weapon.Weapons);
        Apprentice Yuan = new Apprentice("Yuan", "Gaming", "Play", 19, "BladeSpire");
        System.out.println(Yuan.Aura);
        System.out.println(Yuan.University);
        Yuan.BattleCry();

        Destruction Dire = new Destruction();
        CreationAgent Test = new CreationAgent();
        System.out.println(Test.passed);
        



    }
    

}
