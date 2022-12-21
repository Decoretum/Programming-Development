package LearnJava;

public class OOP {
    public static void main (String args[]){
        Weapon ChaosStaff = new Weapon("Staff of Chaos","Abyss");
        Magi Gael = new Magi("Gael", "Destruction & Alteration", "Abyss", 19);
        Gael.BattleCry();
        Gael.PrepWep();
        Gael.Attack();
        Gael.TakeWeapon(ChaosStaff);
    }
    

}
