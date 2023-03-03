public class Playground{
    //loose coupling using Interfaces
    public static void main (String args[]){
        Developer Dev1 = getBackEnd(); //Gael
        Developer Dev2 = getFrontEnd(); //Justin

        Dev1.Motto();

        int debugged = debugBack(90);
        int doubledebug = DoubleDebug(90);

        System.out.println(debugged);
        System.out.println(doubledebug);

        Dev1.ChangeMoney(1000);
    }

    //we directly use the interface instead of the actual classes such as Gael and Justin
    //this leads to multi-inheritance in a way, since we dont need to create dependencies that much, we have a common class(interface) 
    public static Developer getBackEnd(){
        return new Gael();
    }

    public static Developer getFrontEnd(){
        return new Justin();
    }

    public static int debugBack(int num){
        Developer a = new Gael();
        int bug = a.Debug(num);
        return bug;
    }

    public static int DoubleDebug(int num){
        Developer a = new Gael();
        Developer b = new Justin();
        int bug = a.Debug(num) + b.Debug(num);
        return bug;
    }
}