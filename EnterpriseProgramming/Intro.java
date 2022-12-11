package EnterpriseProgramming;
import java.util.*;

public class Intro{
    private String Name = "Gael";
    private int Age = 19;
    private String Specialization = "Enterprise Systems";
    private String CareerPath = "Software Development";

    public void Introduction(){
        System.out.println(String.format("%s is age %d. He specializes in %s for the career of %s",Name,Age,Specialization,CareerPath));
    }

    public static void main(String args[]){
        Intro Gael = new Intro();
        Gael.Introduction();
        
    }
}