package JavaDev.SturdyPackage;
//import JavaDev.MalleablePackage.*;

public class Destruction {
    public static String Affinity = "Dark Justice"; //can be both public and static, wow
    public static int Power;
    protected String Whisper = "Dark be the way to the Core.";
    protected String AgentIntel = "Info regarding Creation\'s minions";
    protected void DarkWhisper(){
        System.out.println(String.format("\"%s\" is the key to Darkness's absoluteness.",this.Whisper));
    }

    public static void Meditate(){
        System.out.println("Absorbing power from deep within!");
        Power++;

    }
    public void Shout(){
        System.out.println(String.format("To emphasize, \"%s\"!",this.Whisper));
    }
    public static void main (String args[]){
        /*
        Creation Visitor = new Creation();
        CreationAgent Spy = new CreationAgent();

        System.out.println(Visitor.Digit);
        System.out.println(Spy.passed);
        */
    }
}
