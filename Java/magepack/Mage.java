package magepack;

enum Absolutes{
    ABYSS,
    LIGHTNING,
    AIR,
    ARCANE
}
public class Mage {
        String Status = "Active";
        int Power = 0;
        String Homeland = "BladeSpire";

        static void Likes(){
            System.out.println("Mages like elemental theory, magical sparring, and textbook reading!");
        }
     
        public void WarCry(){
            System.out.println("");
            System.out.println("I am one with the vitalities of our world!");
        }
    
        public void Information(){
            System.out.println("");
            System.out.println("Homeland: " + Homeland + " with the status of " + Status);
        } 
    
        public void Power(){
            System.out.println("");
            System.out.println("Power: " + Power);
        }

    public class Sorcerer extends Mage{
     
            String name;
            int age;
            String Element;
            String Specialization;
            String Combat = "Ranged Combat";
            String Category = "Support, DPS, AOE";
    
            public class Secrets{
                String Secret = "We need distance in order to fend off the enemy, short-ranged combat is too much!";
                public void Spread(){
                    System.out.println(Secret);
                }
            }
        
            public Sorcerer(String name, int age, String element, String specialization){ //we initialized
                this.name = name;
                this.age = age;
                this.Element = element;
                this.Specialization = specialization;
            }
        
            public void Information(){
                System.out.println(String.format("Homeland: %s with the status of %s.\nName: %s, Age: %d, Element: %s, Specialization: %s",this.Homeland, this.Status, this.name, this.age, this.Element, this.Specialization));
                //alternative for template literals
            } 
        
            public void WarCry(){
                System.out.println("We will bend the Elements to our favor!");
            }
    
        
    }

    public class Spellsword extends Mage {
        //children classes
           String name;
           int age;
           String Element;
           String Specialization;
           String Combat = "Ranged Combat";
           String Category = "Support, DPS, AOE";
       
           public Spellsword(String name, int age, String element, String specialization){ //we initialized
               this.name = name;
               this.age = age;
               this.Element = element;
               this.Specialization = specialization;
           }
       
           public void Information(){
               System.out.println(String.format("Homeland: %s with the status of %s.\nName: %s, Age: %d, Element: %s, Specialization: %s",this.Homeland, this.Status, this.name, this.age, this.Element, this.Specialization));
               //alternative for template literals
           } 
       
           public void WarCry(){
               System.out.println("Let us destroy you with the mighty Arcana of our blade and hand!");
           }
    
   }
     
    



public static void main(String args[]){ //we can debug/run from here, which is within the public class domain
Mage mage = new Mage();
Mage.Sorcerer Gamadan = mage.new Sorcerer("Gamadan", 19, "Lightning", "Destruction");
System.out.println(Gamadan.Combat);
}

}

class main1{
    public static void main2(String args[]){ //we can create new class outside of public class domain, then debug within class
        Mage mage = new Mage();
        Mage.Sorcerer Gamadan = mage.new Sorcerer("Gamadan", 19, "Lightning", "Destruction");
        System.out.println(Gamadan.Combat);
        }
}
