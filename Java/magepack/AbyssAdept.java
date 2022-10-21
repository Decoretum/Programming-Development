package magepack;

public class AbyssAdept extends AbyssGod {
    String Name;
    String Specialization;
    public AbyssAdept(String name, String specialization){
        Name = name;
        Specialization = specialization;
    }

    public void WarCry(){
        System.out.println("I, " + this.Name + "," + " shall devour you with my Abyssal might using " + this.Specialization + "!");
    }

}
