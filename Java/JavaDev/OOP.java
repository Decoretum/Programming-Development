package JavaDev;
import java.util.*;

import JavaDev.SturdyPackage.CreationAgent;
import JavaDev.SturdyPackage.Destruction;

public class OOP {
    public static void main (String args[]){
        Weapon ChaosStaff = new Weapon("Staff of Chaos","Abyss");
        Magi Gael = new Magi("Gael", "Destruction & Alteration", "Abyss", 19);
        Magi Solomon = new Magi("Solomon", "Alteration & Restoration", "Light", 14, "Linda's Light");
        Magi Sinbad = new Magi("Sinbad","Destruction","Lightning",20,"Belark's Thunder");
        Magi[] Magis = new Magi[3];
        ArrayList<Magi> Magises = new ArrayList<>();
        Magises.add(Gael);
        Magises.add(Solomon);
        Magises.add(Sinbad);
        Magis[0] = Gael;
        Magis[1] = Solomon;
        Magis[2] = Sinbad;
        for (int i = 0; i < Magis.length; i++){
            System.out.println(Magis[i].Name());
        }

        for (int i = 0; i < Magises.size(); i++){
            System.out.println(Magises.get(i).Name());
        }
        ArrayList <Object> Artifacts = new ArrayList<>();
        Artifacts.add(Gael);
        Artifacts.add("ME");
        Artifacts.add(12);
        System.out.println(Artifacts);
        System.out.println(Magis[0]);
        System.out.println(Artifacts.get(2));
        Gael.TakeWeapon(ChaosStaff);
        Gael.MagesAura(); //since the Magisaura arraylist is static, we can access it using one of the instances of the Magi class
        Gael.WhatWeapon().WeaponList();
        Apprentice Yuan = new Apprentice("Yuan", "Gaming", "Play", 19, "BladeSpire");
        Yuan.BattleCry();

        Destruction Dire = new Destruction();
        CreationAgent Test = new CreationAgent();
        System.out.println(Test.passed);
        Yuan.LearnNew();
        



    }
    

}
