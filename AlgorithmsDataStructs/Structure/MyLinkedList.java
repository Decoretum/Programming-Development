package AlgorithmsDataStructs.Structure;
// Doubly Linked List
public class MyLinkedList {
    MyLinkedList next;
    MyLinkedList prev;
    MyLinkedList head;
    int val;
    
    public MyLinkedList() { //or node
        this.val = 1001;
        this.head = this;
        this.next = null;
        this.prev = null;
    }
    
    public MyLinkedList(int val){
        this.val = val;
        this.head = this;
        this.next = null;
        this.prev = null;
    }
    
    public int get(int index) {
        MyLinkedList current = this.head;
        int i = 0;
        try{
            while (current.next != null && i < index){
            current = current.next;
            i++;
            } 
            if (index > i) {
                return -1;
            } else if (index == 0){
                if (current.val == -1  || current.val == 1001){
                    return -1;
                }
            }
            return current.val;
        } catch (Exception e) {
            return -1;
        }
        
    }
    
    public void addAtHead(int val) {
        MyLinkedList New = new MyLinkedList(val);
        if (this.head.val == 1001 || this.head == null){
            this.head = New;
            this.val = New.val;
        } else {
            MyLinkedList former = this.head;
            former.prev = New;
            New.next = former;
            this.head = New;
        }
    }
    
    public void addAtTail(int val) {
        MyLinkedList current = this.head; 
        while (current.next != null){
            current = current.next;
        } if (current.val == 1001) {
            MyLinkedList New = new MyLinkedList(val);
            this.head = New;
        } else {
            MyLinkedList New = new MyLinkedList(val);
            current.next = New;
            New.prev = current;
        }
    }
    
    public void addAtIndex(int index, int val) {
        int counter = 0;
        MyLinkedList current = this.head;
        try{
            while (counter != index && current.next != null){
                current = current.next;
                counter++;
            } if (index >= counter+2){} 
            else if (current.next == null){
                if (counter != index){
                    MyLinkedList New = new MyLinkedList(val);
                    current.next = New;
                    New.prev = current;
                } else if (counter == 0) {
                    MyLinkedList New = new MyLinkedList(val);
                    MyLinkedList former = this.head;
                    this.head = New;
                    New.next = former;
                    former.prev = New;
                } else {
                    MyLinkedList New = new MyLinkedList(val);
                    MyLinkedList beforecurrent = current.prev;
                    MyLinkedList aftercurrent = current.next;
                    beforecurrent.next = New;
                    New.prev = beforecurrent;
                    New.next = current;
                    current.prev = New;
                }             
            } else {
                if (counter == 0){
                    MyLinkedList New = new MyLinkedList(val);
                    MyLinkedList former = current;
                    MyLinkedList after = current.next;
                    New.next = former;
                    former.prev = New;
                    New.next = after;
                    after.prev = New;
                    this.head = New;
                } else {
                    MyLinkedList New = new MyLinkedList(val);
                    MyLinkedList beforecurrent = current.prev;
                    MyLinkedList aftercurrent = current.next;
                    beforecurrent.next = New;
                    New.prev = beforecurrent;
                    New.next = current;
                    current.prev = New;
                }
            }
        
        } catch (Exception e){
            System.out.println(e);
        }
        
    }
    
    public void deleteAtIndex(int index) {
        int counter = 0;
        try{
            MyLinkedList current = this.head;
            while (counter < index && current.next != null){
                current = current.next;
                counter++;
            } if (counter == 0){
                if (counter != index){} 
                else if (current.prev == null && current.next == null && index == counter){ //just 1 node
                    this.head.val = -1;
                } else { //more than 1 node
                    MyLinkedList after = current.next;
                    current.next = null;
                    after.prev = null;
                    this.head = after;

                }
            } else if (counter < index){} 
            else if (current.next == null) { //last
                MyLinkedList before = current.prev;
                before.next = null;
                current.prev = null;
            } else { //has before and current
                MyLinkedList before = current.prev;
                MyLinkedList after = current.next;
                before.next = after;
                after.prev = before;
            }
            
        } catch (Exception e){
            System.out.println(e);
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */