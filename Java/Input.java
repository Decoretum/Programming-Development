
import magepack.*;
import DataStructuring.*;
import ObjectsSystem.*;

import java.util.*;
public class Input {
    public static void main (String args[]){
       Mage mage = new Mage();
       Mage.Sorcerer Decoretum = mage.new Sorcerer("Decoretum", 19, "Abyss", "Destruction & Alteration");
       Mage.Spellsword Pontrilius = mage.new Spellsword("Pontrilius", 19, "Lightning", "Blade, Destruction, & Alteration");

       Decoretum.Information();
       Decoretum.WarCry();
       System.out.println("");

       Pontrilius.WarCry();
       Pontrilius.Information();
       System.out.println("");

       //higher mages, public classes within a public main class, hence inner public classes
       HigherMages highmage = new HigherMages();
       HigherMages.ArchSorcerer DecoretumtheGreat = highmage.new ArchSorcerer("Decoretum",19,"Abyss","Destruction, Alteration, & Conjuration");
       HigherMages.Necromancer Absalon = highmage.new Necromancer("Absalon", 19, "Lightning", "Destruction & Restoration");
       DecoretumtheGreat.Arrogance();
       DecoretumtheGreat.Abilities();
       DecoretumtheGreat.Quote();
       Absalon.Quote();

       

       //abyss category
        AbyssGod DarkMother = new AbyssGod();
        AbyssAdept DarkAdept = new AbyssAdept("Malborn", "Destruction & Conjuration");
        DarkMother.WarCry();
        DarkAdept.WarCry();

        System.out.println("");

        //trying out structuring
        HashMap<Object,Object>ErrorObject = new HashMap<Object,Object>();
        ErrorObject.put(false,"Killed a lion");
        ErrorObject.put(123124,"Destroyed Worlds");
        ErrorObject.put(true, "Defied the devil");
        ErrorObject.put(1231, true);
        
        DataStructures2 Gael = new DataStructures2();
        Gael.ObjectFilter(ErrorObject);

        System.out.println("\n\n\n");

        //PersonObject

        /* 
        Son Haha = new Son();
        Haha.Pride();  an example of separate classes in separate files with inheritance
        */

        System.out.println("\n\n\n\n");
        int[]array = {12,312,12,414,1222};
        Functions.ArraySum(array);

        GaelChild Publicity = new GaelChild();
        Publicity.OnlyPublic();
        GaelChild.CanBeStatic();

        int[] TestArray = Functions.ManipulatedArray(array);
        for (int i : TestArray){
            System.out.println(i);
        }

        Gael Tinie = new Gael("Tinie");
    }
}
