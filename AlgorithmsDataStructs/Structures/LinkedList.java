

public class LinkedList {
    Node head;

    LinkedList(Node A){
    this.head = A;
    } 

    LinkedList(String A){
        Node node = new Node(A);
        this.head = node;
    }

    void printList(){
        Node current = this.head;
        String list = current.getData();
        while (current.next != null){
            current = current.next;
            list = list + " -> " + current.getData();
        }
        System.out.println(list);
    }

    void addNode(Node A){
        Node current = this.head;
        while (current.next != null){
            current = current.next;
        }
        current.next = A;
    }

    void addNode(String A){
        Node node = new Node(A);
        Node current = this.head;
        while (current.next != null){
            current = current.next;
        }
        current.setNext(node);
    }

    void insertNode(int position,String A){
        Node node = new Node(A);
        Node before = null;
        Node current = this.head;
        int index = 0;
        while (current.next != null && index < position){
            index++;
            before = current;
            current = current.next;
        }
        before.unlink();
        before.setNext(node);
        node.setNext(current);
        System.out.println(before.getData());
    }

    void insertNode(int position,Node A){
        Node before = null;
        Node current = this.head;
        int index = 0;
        while (current.next != null && index < position){
            index++;
            before = current;
            current = current.next;
        }
        before.unlink();
        before.setNext(A);
        A.setNext(current);
        System.out.println(before.getData());
    }

    void replace(String oldData, String newData){ //using data method
        byte cond = 0;
        Node New = new Node(newData);
        Node before = null;
        Node current = this.head;
        Node after = null;
        while(current.next != null){
            if (current.getData() == oldData){
                if (current == this.head){
                    after = current.next;
                    this.head.unlink();
                    this.head = New;
                    New.setNext(after);
                    cond = 1;
                    break;
                }
                else{
                    after = current.next;
                    before.unlink();
                    current.unlink();
                    before.setNext(New);
                    New.setNext(after);
                    break;
                }
            }

            else {
                before = current;
                current = current.next;
            }
        }

        if (cond == 0){
            after = current;
            before.unlink();
            before.setNext(New);
        }    
        }
    
    void replace(int index, String data){ //using position method
        Node node = new Node(data);
        int i = 0;
        Node before = null;
        Node current = this.head;
        Node after = null;
        if (index == 0){
            after = current.next;
            this.head.unlink();
            node.setNext(after);
            this.head = node;
        }
        else{
            while (current.next != null && i < index){
                before = current;
                current = current.next;
                i++;
            }
            after = current.next;
            before.unlink();
            current.unlink();
            before.setNext(node);
            node.setNext(after);
        }
    }

    void Remove(int index){
        Node before = null;
        Node current = this.head;
        Node after = null;
        int i = 0;
        if (index == 0){
            after = current.next;
            this.head.unlink();
            this.head = after;
        }
        else{
            while(current.next != null && i < index){
                before = current;
                current = current.next;
                i++;
            }
            after = current.next;
            before.unlink();
            current.unlink();
            before.setNext(after);
        }
    }

    void Pop(){
        Node next = this.head.next;
        this.head.unlink();
        this.head = next;
    }
}
