package LearnJava;
import javax.swing.*;

public class GUI {
    public static void main (String args[]){
        String name = JOptionPane.showInputDialog("What is your name?");
        JOptionPane.showMessageDialog(null, "Hello, " + name);

        int age = Integer.parseInt(JOptionPane.showInputDialog("What is your age?"));
        JOptionPane.showMessageDialog(null,String.format("Good day, %s. You are %d years old.",name,age));
    
        
    }
    
}
