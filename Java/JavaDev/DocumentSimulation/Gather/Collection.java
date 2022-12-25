package JavaDev.DocumentSimulation.Gather;
import JavaDev.DocumentSimulation.Reports.*;

public class Collection {
  private String ReportDate;
  private String Gatherer;
  private String ReportData;
  private Report ReportResult;

  Collection(String date, String person, String data){
    this.ReportDate = date;
    this.Gatherer = person;
    this.ReportData = data;
  }

  public void Fixdate(){ //if date is formatted correctly
    
  }
}
