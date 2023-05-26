package Algorithms;
import java.util.*;
//import Structures.Tree;


//https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
public class Trees{

    //traverse Root, left subtree, then right subtree
    static void PreOrderIterative(Tree root){
        if (root == null){
            return;
        }

        Stack<Tree> st = new Stack<>();
        Tree current = root; //current before iterations

        //current here is the current before iterations
        while (!st.isEmpty() || current != null){ 

            //This will run until Tree traversed will be null
            while (current != null){
                System.out.println(current.value + " ");
                if (current.right != null){
                    st.push(current.right);
                }
                current = current.left;

            }

            //If tree traversed is null, then current tree will be first tree in stack
            if (!st.isEmpty()){
                current = st.pop();
            }

        }
        
    }

    static void PreOrderRecur(Tree root){
        if (root == null){
            return;
        }
        System.out.println(root.getValue());
        PreOrderRecur(root.left);
        PreOrderRecur(root.right);
    }

    //Traverse, left subtree, root, then right subtree
    static void InOrderIterative(Tree root){
        Stack<Tree> stack = new Stack<>();
        Tree current = root;
        while (!stack.isEmpty() || current != null){
            /* We basically traverse all left nodes since we will use them as reference 
            values as "root" to come back to
            */
            while (current != null){
                //System.out.println("Current is " + current.getValue());
                stack.push(current);
                current = current.left;
            }
            
            /* Whether node comes from the right or left(or is null), the node is still a part of the stack 
            Using pop, we move 1 level up in the tree and traverse this node,
            then we traverse the right children and traverse the left children of these right children  */
            current = stack.pop();
            System.out.println(current.getValue());
            current = current.right;
        }
    }

    static void InOrderRecur(Tree root){
        if (root == null){
            return;
        }
        InOrderRecur(root.left);
        System.out.println(root.getValue());
        InOrderRecur(root.right);
    }

    //traverse left subtrees then right subtrees
    static void PostOrderItera(Tree root){
        
    }



    //public void PreOrderIterative()
    public static void main (String args[]){
        Tree Main = new Tree(100);
        Tree L1 = new Tree(90);
        Tree L2 = new Tree(80);
        Tree M1 = new Tree(70);
        Tree M2 = new Tree(60);
        Tree N1 = new Tree(88);
        Tree N2 = new Tree(65);
        Tree O1 = new Tree(82);
        Main.addLeft(L1);
        Main.addRight(L2);
        L1.addLeft(M1);
        L1.addRight(N1);
        L2.addRight(M2);
        M2.addLeft(N2);
        N1.addLeft(O1);
        PreOrderIterative(Main);
        //InOrderIterative(Main);

    }
}

class Tree{
    Object value;
    Tree left;
    Tree right;

    Tree(Object value){
        this.value = value;
    }

    Tree(Object value, Tree left, Tree right){
        this.value = value;
        this.left = left;
        this.right = right;
    }

    Tree(Object value, Tree left, String where){
        if (where.equals(left)){
            this.value = value;
            this.left = left;
        }
        else if (where.equals(right)){
            this.value = value;
            this.right = right;
        }
    }


    //methods
    void addLeft(Tree left){
        this.left = left;
    }

    void addRight(Tree right){
        this.right = right;
    }

    Object getValue(){
        return this.value;
    }

    Tree getLeft(){
        return this.left;
    }

    Tree getRight(){
        return this.right;
    }
}

