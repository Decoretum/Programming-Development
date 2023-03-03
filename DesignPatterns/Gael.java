public class Gael implements Developer{
    private int Money = 19;
    //class focuses on Back-end
    //includes Interfaces(Coupling), and Encapsulation(Access Modifiers)
    @Override
    public void Motto(){
        System.out.println("I\'m usually programming as a back-end developer");
    }

    //setter
    public void ChangeMoney(int change){
        this.Money = change;
        System.out.println("Money changed to " + Money);
    }
 
    public int Debug(int num){
        int final1 = num * 69;
        return final1;
    }




    public void SystemDesign(){
        System.out.println("Let me use ERDs, Relation Tables, and Use Case Diagrams");
    }
}