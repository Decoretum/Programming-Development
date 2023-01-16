package JavaDev.SturdyPackage;
//import JavaDev.MalleablePackage.*;

public class CreationAgent extends Creation {
    public String passed = this.Code; //protected variable became public
    
    public void Decode(){
        System.out.println(String.format(" \"%s\" proves my nature as Creation's agent.",this.Code));
    }
    public static void main (String args[]){
        /*CreationAgent Light = new CreationAgent();
        Light.Decode();
        Light.Relay();

        Destruction Monster = new Destruction();
        Monster.DarkWhisper(); */
    }
}
