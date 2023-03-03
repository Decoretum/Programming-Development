package AlgorithmsDataStructs;
import java.util.*;

public class Tree{
    Object value;
    Tree left;
    Tree right;

    public Tree(Object value){
        this.value = value;
    }

    public Tree(Object value, Tree left, Tree right){
        this.value = value;
        this.left = left;
        this.right = right;
    }

    public Tree(Object value, Tree left, String where){
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
    public void addLeft(Tree left){
        this.left = left;
    }

    public void addRight(Tree right){
        this.right = right;
    }

    public Object getValue(){
        return this.value;
    }

    public Tree getLeft(){
        return this.left;
    }

    public Tree getRight(){
        return this.right;
    }
}