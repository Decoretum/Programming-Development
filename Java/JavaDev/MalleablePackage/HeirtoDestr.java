package JavaDev.MalleablePackage;
import JavaDev.SturdyPackage.*;

public class HeirtoDestr extends Destruction {
    int MinionPower = 0;

    void Celebrate(){
        if (this.Power < 2){
            System.out.println("Still not enough to be powerful!");
        }

        else {
            System.out.println("Growing stronger by the day!");
        }
    }

    void PowerCompare(){
        if (this.MinionPower < this.Power){
            System.out.println("You cannot overthrow the overlord!");
        }
        else{
            System.out.println("You just might have a chance to be overlord...");
        }
    }
    public static void main (String args[]){
        HeirtoDestr Bater = new HeirtoDestr();
        HeirtoDestr Hater = new HeirtoDestr();
        Hater.Meditate();
        Bater.Meditate();
        Bater.DarkWhisper();
        Bater.Shout();
        System.out.println(Bater.Affinity);
        System.out.println(String.format("Power: %d",Bater.Power));
        Bater.Celebrate();
        Bater.PowerCompare();
        
    }
}
