package JavaDev.DocumentSimulation.Reports;
import JavaDev.DocumentSimulation.Gather.*;;

public class Report {
    static int ReportNumber;
    private CollectionReport Doc;
    public Report(CollectionReport Doc){
        this.Doc = Doc;
        this.Initialize();
    }
    public void Initialize(){
        ReportNumber++;
        int copy = ReportNumber;
        String Header = String.format("Report: \"%s\". Taken on %s.", this.Doc.Header(),this.Doc.Date());
        String Body = String.format("Report Content: %s",this.Doc.Body());
        String End = String.format("Report Conclusion: %s",this.Doc.Conclusion());
        String Person = String.format("Reporter: %s",this.Doc.Person());
        System.out.println(String.format(" ------- START OF REPORT %d --------- ",copy));
        System.out.println(Header);
        System.out.println(Body);
        System.out.println(End);
        System.out.println(Person);
        System.out.println(String.format(" ------- END OF REPORT %d --------- ",copy));
    }
}
