package JavaDev.DocumentSimulation.Gather;
import JavaDev.DocumentSimulation.Reports.*;

public class CollectionReport {
  private String ReportDate;
  private String Gatherer;
  private String ReportHeader;
  private String ReportBody;
  private String ReportConclusion;

  public CollectionReport(String date, String person, String Header, String Body, String End){
    this.ReportDate = date;
    this.Gatherer = person;
    this.ReportHeader = Header;
    this.ReportBody = Body;
    this.ReportConclusion = End;
  }

  public String Date(){
    return this.ReportDate;
  }

  public String Person(){
    return this.Gatherer;
  }

  public String Header(){
    return this.ReportHeader;
  }

  public String Body(){
    return this.ReportBody;
  }

  public String Conclusion(){
    return this.ReportConclusion;
  }
}
