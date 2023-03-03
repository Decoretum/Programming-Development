package AlgorithmsDataStructs;
import java.util.*;

public class Play{
    static Queue<Object> mine1 = new ArrayDeque<>();
    static void InOrder(Tree node){
        if (node == null){
            return;
        }
        InOrder(node.getLeft());
        mine1.add(node.getValue());
        InOrder(node.getRight());
        
    }
    public static void main (String args[]){
        Tree Bro = new Tree(100);
        Tree left = new Tree(80);
        Tree right = new Tree(90);
        Tree down = new Tree(70);

        //setting the connections
        Bro.addLeft(left);
        Bro.addRight(right);
        left.addRight(down);
        
        //inorder traversal
        //display/get tree nodes in non-decreasing order
        InOrder(Bro);
        System.out.println(mine1);
    }
}