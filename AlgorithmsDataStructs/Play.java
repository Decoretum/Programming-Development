package AlgorithmsDataStructs;
import java.util.*;

public class Play{

    static Queue<Object> mine1 = new ArrayDeque<>();
    //Tree traversals for Binary Trees (perfect binary trees)

    //Traverses Binary tree by starting with the lowest elements up to highest elements
    //Left subtrees -> root node --> right trees
    static void InOrder(Tree node){
        if (node == null){
            return;
        }
        InOrder(node.getLeft());
        mine1.add(node.getValue());
        InOrder(node.getRight());
        
    }

    //Traverses Binary Tree by displaying the tree node, then left subtrees -> right subtrees
    static void PreOrder(Tree node){
        if (node == null){
            return;
        }
        mine1.add(node.getValue());
        PreOrder(node.getLeft());
        PreOrder(node.getRight());
    }

    //Traverses Binary Tree by starting first with display of left subtrees, then the right subtrees -> root node
    static void PostOrder(Tree node){
        if (node == null){
            return;
        }
        PostOrder(node.getLeft());
        PostOrder(node.getRight());
        mine1.add(node.getValue());
    }

    public static void main (String args[]){
        Tree Bro = new Tree(100); //0
        Tree left = new Tree(80); //1
        Tree right = new Tree(90); //1
        Tree down = new Tree(70); //2
        Tree rand = new Tree(50); //2
        Tree rand1 = new Tree(69); //2

        //setting the connections
        Bro.addLeft(left);
        Bro.addRight(right);
        left.addRight(down);
        left.addLeft(rand1);
        right.addLeft(rand);
   
        //InOrder(Bro);
        //PreOrder(Bro);
        //PostOrder(Bro);
        System.out.println(mine1);
    }
}