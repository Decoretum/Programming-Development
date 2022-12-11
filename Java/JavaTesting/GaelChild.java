package JavaTesting;
public class GaelChild{ //another class that could access GaelClass attributes and methods
    private String Secret = "I'm still a virgin!!";
    public void OnlyPublic(){
        System.out.println("Only public!");
        System.out.println("My secret is " + Secret);
    }

    static void CanBeStatic(){
        System.out.println("Static is the best!");
    }

    public static void main(String[]arg){
        GaelClass GaelKid1 = new GaelClass("Gael","Ateneo de Manila University","BS MIS, Specialization in Data Science and Analytics","3rd Year",'M',"Single");
        GaelKid1.status = "Taken"; //we modify attribute of an object from a different class
        GaelKid1.Emotion = "Feeling happy!"; //we initialize a value for the empty variable "Emotion" of object from a class
        System.out.println(GaelKid1.Information());
        GaelKid1.Greetings();
        GaelKid1.GreetingswithName();
        GaelKid1.Education();
        GaelKid1.Love();
        GaelKid1.ChangeStatus("Single");
        GaelKid1.Love();
        System.out.println("Gael\'s Hardships/Challenges");
        

    }
}