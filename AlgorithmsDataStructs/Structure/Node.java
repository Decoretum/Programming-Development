package AlgorithmsDataStructs.Structure;
import java.util.*;

public class Node {
    String data;
    Node next;
    ArrayList<Node>Connected = new ArrayList<>();
    

    public Node(String data){
        this.data = data;
    }

    public String getData(){
        return this.data;
    }

    public void Connect(Node node){
        Connected.add(node);
    }
    
    public void Connections(){
        System.out.println(this.getData());
        for (Node node : Connected){
            System.out.println("--> " + node.getData());
        }
        System.out.println("");
    }

    public Node getNext(){
        return this.next;
    }

    public void setNext(Node A){
        this.next = A;
    }

    public void unlink(){
        this.next = null;
    }
    
}
