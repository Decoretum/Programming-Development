package JavaDev.DocumentSimulation.Gather;
import JavaDev.DocumentSimulation.Reports.*;
import java.util.*;
import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;

public class CollectionReport {

  public CollectionReport(){ //String date, String person, String Header, String Body, String End
  }

  public String Date(){
    DateTimeFormatter Day = DateTimeFormatter.ofPattern("MM/dd/yyyy");
    DateTimeFormatter Time = DateTimeFormatter.ofPattern("HH:mm:ss");
    LocalDateTime Datinst = LocalDateTime.now();
    LocalDateTime Timeinst = LocalDateTime.now();
    String Label = String.format("Report Date: %s at the time of %s",Day.format(Datinst),Time.format(Timeinst));
    return Label;
  }

  public String Person(){
    System.out.println("Reporter:");
    Scanner input = new Scanner(System.in);
    String person;
    while (true){
      person = input.nextLine();
      if (Character.isUpperCase(person.charAt(0))){
        break;
      }
      else{
        System.out.println("Person\'s first digit must be uppercase");
      }
    }

    return person;
  

  }

  public String Header(){
    System.out.println("Report Header:");
    Scanner input = new Scanner(System.in);
    String Head = input.nextLine();
    
    return Head;
  }

  public String Body(){
    ArrayList <String> Entries = new ArrayList<>();
    System.out.println("Report Content");
    Scanner input = new Scanner(System.in);
    while (true){
      String Entry = input.nextLine();
      if (Entry.equals("DONE") || Entry.equals("done")){
        break;
      }
      else{
        Entries.add(Entry);
      }
      
    }
    
    String finalone = "";
    for (int i = 0; i <= Entries.size() - 1; i++){
      finalone += "\n" + Entries.get(i);
    }

    return finalone;
  }

  public String Conclusion(){
    System.out.println("Report Conclusion:");
    Scanner input = new Scanner(System.in);
    String end = input.nextLine();
    return end;
  }
}
