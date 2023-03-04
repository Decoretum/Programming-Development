

public class Node {
    String data;
    Node next;

    Node(String data){
        this.data = data;
    }

    String getData(){
        return this.data;
    }

    Node getNext(){
        return this.next;
    }

    void setNext(Node A){
        this.next = A;
    }

    void unlink(){
        this.next = null;
    }
    
}
