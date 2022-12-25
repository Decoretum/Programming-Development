package JavaDev.MalleablePackage;
import JavaDev.SturdyPackage.*;

public class Creation {
    public byte Digit = 5; //public can be accessed by files from different packages within same package/folder
    protected String Code = "None shall pass"; //can be accessed similar to public but accessor must be sublcass of class containing protected
    private int Power = 9012; //can only be accessed by this class, but can be put to functions used by public and protected

    protected void Relay(){
        System.out.println(String.format("%d is the power of Creation. Heed this",this.Power));
    }
    public static void main (String args[]){
        CreationAgent Land = new CreationAgent();
        Land.Relay();
        Creation God = new Creation();
        System.out.println(String.format("%d is the Power of our God.", God.Power));
    }
}
