package JavaDev.DocumentSimulation.Outcome;
import JavaDev.Collection;
import JavaDev.DocumentSimulation.Gather.*;
import JavaDev.DocumentSimulation.Outcome.*;
import JavaDev.DocumentSimulation.Reports.*;

public class Page1 {
    public static void main(String [] args){
        String Body1 = "Gael spent majority of his time programming, coding, creating a Web applicaiton, as well as programming in Java and Python";
        String Conc1 = "Despite Gael\'s programming journey during his vacation, he still found time to do other meaningful acivities.";
        CollectionReport Doc1 = new CollectionReport("12/25/2022","Gael","Christmas Special",Body1,Conc1);
        Report FinalDoc1 = new Report(Doc1);

    }
}
