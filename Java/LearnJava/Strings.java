package LearnJava;

public class Strings {
    static String name = "Gael";
    static String stringy = "    ";
    static String Impostor = "123";
    public static void main (String args[]){
        System.out.println(name.length());
        System.out.println(name.equalsIgnoreCase("GaEL"));
        System.out.println(name.charAt(0));
        System.out.println(name.indexOf("e"));
        System.out.println(stringy.isEmpty());
        System.out.println(stringy.isBlank()); 
        System.out.println(name.replace("a","e"));
        int a = Integer.parseInt(Impostor);
        System.out.println(a+3);

        //printf() for formatted string or sysout.print(String.format())
        // %b for for boolean
        // %s for string
        // %c for characters
        // %d for integers
        // %f for doubles

        // before conversion character, we have width to allocate number of spaces (includes space of name)
        // ex. %10s
        // we can justify text by putting "-" on width to be allotted to the right of the character

        //precision
        //added before conversion character to specify number of digits

        double d1 = 3.1412;
        System.out.printf("We have a %.3f!",d1);

        //flags
        // adds effect to output by adding it before conversion character
        // - : left justify
        // + or - for numeric value
        // , if number > 1000

        int d2 = 141241;
        System.out.println(String.format("%,d is our lucky number!",d2));


    }
}
