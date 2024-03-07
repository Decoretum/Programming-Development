package AlgorithmsDataStructs.Structure;
import java.util.*;


public class JavaStructs{
    public static void main (String args[]){
        Stack<String> my = new Stack<>();

        //Stack Interface
        my.push("Gael");
        my.push("You");
        my.push("Dame");
        my.push("Sand");
        String popped = my.pop();
        String peeking = my.peek();

        //Queue interface
        //poll pops head and returns it
        //remove removes certain element on any position, first occurrence of element is removed
        //add() adds at end of Queue
        //Implemented by LinkedList, PriorityQueue

        //Since this is linked list, I know this uses pointers (pointing to next) and self data,
        //wherein every element is a node object
        Queue<String> MyQueue = new LinkedList<>();
        MyQueue.add("Gael");
        MyQueue.add("92");
        MyQueue.add("721");
        MyQueue.add("Dame");
        System.out.println("Queue for now is " + MyQueue);
        System.out.println("Head is " + MyQueue.peek());
        System.out.println("Popped is " + MyQueue.poll());
        System.out.println("Queue for now is " + MyQueue);
        MyQueue.remove("721");
        System.out.println("Queue for now is " + MyQueue);

        //Queue implemented by Priority Queue, where elements are prioritized first
        Queue<Integer> Two = new PriorityQueue<>();
        Queue<String> Words = new PriorityQueue<>();
        Two.add(9);
        Two.add(0);
        Two.add(20);
        Words.add("Gael");
        Words.add("Abel");
        Words.add("Sam");
        Words.add("Mitchel");
        Words.add("Darrel");
        System.out.println("PrioQueue is " + Two);
        System.out.println("Head is " + Two.peek());
        int popped1 = Two.poll();
        System.out.println("After popping " + Two);
        System.out.println("Words Queue: " + Words);
        String popped2 = Words.poll();
        System.out.println("Head of word " + Words.peek());
        Words.remove("Sam");
        System.out.println("PrioQueue" + Words);
        System.out.println("\n\n");

        //Deque, subtype of the queue interface (Hence, it is a separate interface). 
        //implemented by Arraydeque and LinkedList classes
        //It is a double-ended queue that 
        //adds and removes from top and end of data structure
        /* 
        add() / addLast() / offer() - add at last
        addFirst() / push() / offerFirst() - add at first
        removeFirst() - remove first
        removeLast() - remove last
        poll() - is identical to pop(), but this doesnt return exception when deque is empty,
        pollFirst(), pollLast()

    
        */
        Deque<Integer> deq = new LinkedList<>();
        deq.add(9);
        deq.add(10);
        deq.add(72);
        deq.add(82);
        deq.offer(90);
        deq.removeFirst();
        System.out.println(deq);


        //LinkedLists
        /*
        Containers (nodes) that point to a next container (node)
        add first, add last, remove first, remove last,
        get first, get last
         */
        LinkedList <String> GaelList = new LinkedList<>();
        GaelList.add("Yo");
        GaelList.add("Mama");
        GaelList.add("HasLove");



    }
}

/*

*/