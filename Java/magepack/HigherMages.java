package magepack;

public class HigherMages  {
    String Status = "Active";
    int Power = 0;
    
    public void Wisdom(){
        System.out.println("The Arcane are for those who seek to understand the world better with their own heart and soul.");
    }

    public void Arrogance(){
        System.out.println("We are power overwhelming, no one or nothing can stop us at our level.");
    }
    
    public class ArchSorcerer extends HigherMages{
        String name;
        int age;
        String Element;
        String Specialization;
        String Combat = "Ranged Combat";
        String Category = "Support, DPS, AOE";
        String Abilities[] = {"Fuse elemental energies into integrated and concentrated spheres of energy","Morph into elemental constructs",
        "Seamless transition from one element to another"};

        public ArchSorcerer(String name, int age, String element, String specialization){
            this.name = name;
            this.age = age;
            this.Element = element;
            this.Specialization = specialization;

        }

        public void Abilities(){
            System.out.println("Abilities of" + this.name + ":");
            for (int c=0; c<Abilities.length; c++){
                System.out.println(Abilities[c]);
            }
        }

        public void Quote(){
            System.out.println("With the aid of " + this.Specialization + "," + " I shall command the Arcane for " + this.Specialization + " using " + this.Element + " for I am " + this.name + "!");
        }
    }

    public class Necromancer extends HigherMages{
        String name;
        int age;
        String Element;
        String Specialization;
        String Combat = "Ranged Combat";
        String Category = "Support, DPS, AOE";
        String Abilities[] = {"Use the Dark Arts to siphon life and energy from your foe","Summon undead constructs",
        "Utilize undead souls for soul harvestation"};

        public Necromancer(String name, int age, String element, String specialization){
            this.name = name;
            this.age = age;
            this.Element = element;
            this.Specialization = specialization;

        }

        public void Abilities(){
            System.out.println("Abilities of" + this.name + ":");
            for (int c=0; c<Abilities.length; c++){
                System.out.println(Abilities[c]);
                }
            }
            
            public void Quote(){
                System.out.println(String.format("I, %s, have walked the planes of Underworld and have became overwhelmingly powerful with my Dark Arts!", this.name));
                System.out.println(String.format("Let my Dark Arts be used for %s while using the power of %s in order to siphon the Life from my enemies!", this.Specialization, this.Element));
            }
    






    }

    public static void main(String args[]){
        HigherMages start = new HigherMages();
        Necromancer G = start.new Necromancer("Abaddon", 2101, "Darkness", "Defense and Offense");
        System.out.println(G.Status);

    }
}
