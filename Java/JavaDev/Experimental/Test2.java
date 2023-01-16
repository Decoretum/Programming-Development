package Experimental;
import Applicational.*;

public class Test2{
    private String Code = "Goolagoo";
    public void Transmithere(){
        System.out.println("Transmitting");
        System.out.println(Code);
    }
    public static void main (String args[]){
        Test1 Intro = new Test1();
        Intro.Transmit();
    }
}