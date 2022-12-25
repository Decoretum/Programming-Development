package JavaDev;

//method name + method parameters = unique method signature

public class Method {
    static int Quant(int a, int b){
        int c = a + b;
        return c;
    }

    static int Quant(int a, int b, int c){
        int d = a + b + c;
        return d;
    }

    static int Quant(String a, String b){
        int c = 1 + 2;
        return c;
    }

    public static void main (String args[]){
        System.out.println(Quant("Gael", "Estrera"));
    }
}
