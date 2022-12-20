package LearnJava;

public class Strings {
    static String name = "Gael";
    static String stringy = "    ";
    public static void main (String args[]){
        System.out.println(name.length());
        System.out.println(name.equalsIgnoreCase("GaEL"));
        System.out.println(name.charAt(0));
        System.out.println(name.indexOf("e"));
        System.out.println(stringy.isEmpty());
        System.out.println(stringy.isBlank()); 
        System.out.println(name.replace("a","e"));
    }
}
