package AlgorithmsDataStructs.Algorithms;

import AlgorithmsDataStructs.Structure.LinkedList;
import AlgorithmsDataStructs.Structure.Node;

public class Alg5 {
    public static void main (String args[]){
        LinkedList Gael = new LinkedList("99");
        Node Cube = new Node("99");
        Gael.addNode("31");
        Gael.addNode("42");
        Gael.printList();
        Gael.insertNode(1, "54");
        Gael.printList();
        Gael.insertNode(3, "62");
        Gael.printList();
        Gael.insertNode(2, Cube);
        Gael.printList();
        Gael.replace("99", "89");
        Gael.printList();
        Gael.replace("54", "81");
        Gael.printList();
        Gael.replace("42", "1");
        Gael.printList();
        Gael.replace(1, "gael");
        Gael.printList();
        Gael.replace(0, "gael");
        Gael.printList();
        Gael.replace(5,"End");
        Gael.printList();
        Gael.Remove(2);
        Gael.printList();
        Gael.Pop();
        Gael.printList();
    }
    
}
