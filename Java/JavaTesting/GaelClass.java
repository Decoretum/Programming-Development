package JavaTesting;
public class GaelClass{ //for objected oriented programming, class should always start with uppercase letter, set out all the variables
// initializer of default values, similar to def __init__ in python
String School;
String Year;
String Emotion;
String Name;
String status;
char Sex;
String Course;
String Challenges [];
private String Secrets [] = {"Horny and motivated to make love"};

public GaelClass(String name, String school, String course, String year, char sex, String stats){ //, called when an object of this class is created, hence fill parameters when creating object of class
    Name = name;
    School = school;
    Course = course;
    Year = year;
    Sex = sex;
    status = stats;
}

/*static methods can be accessed without creating an object of the class. If you want to use attributes of an object of a class, 
use public methods in order to access public/non-static attributes or variables  */
public String Information(){ 
String Information = "Object Name:" + " " + Name + "." + " " + Name + " has status of" + " " + status + "" + " with the sex of" + " " + Sex + "" + "." + "\nEmotion is" + " " + Emotion;
return Information;
}

public void ChangeStatus(String s){
    this.status = s;
    System.out.println(Name + " is now " + s);
}


public void Greetings(){
    System.out.println("Greetings! Nice to meet you!");
}

public void GreetingswithName(){
    System.out.println("Greetings! My name is" + " " + Name);
}

public void Education(){
    System.out.println(Name + "" + " studies in" + " " + School + " in " + Year + " with a course of " + Course);
}

public void Love(){
    if (status == "Single"){
        System.out.println(Name + " is still not taken!");
    }
    else if (status == "Taken"){
        System.out.println(Name + " is already taken :( ");
    }
}

    public static void main(String[]args){
        GaelClass Object1 = new GaelClass("Iris","UP Diliman","Journalism","Post Graduate",'F',"Mother"); //we make an instance object for the class
        GaelClass Object2 = new GaelClass("Joanah","UP Diliman","Civil Engineering","3rd Year",'F',"Single");
        System.out.println(Object1.School + " " + Object1.Year);
        System.out.println(Object2.status + " " + Object2.Sex);
        System.out.println(Object1.Course + " " + Object2.Course);
         for (int a = 0; a < Object1.Secrets.length; a++){
            System.out.println(Object1.Secrets[a]);
        }
    }
}