import java.util.*;
public class Graphs{
    /* 
    Insertion of Nodes/Edges in the graph – Insert a node into the graph.
    Deletion of Nodes/Edges in the graph – Delete a node from the graph.
    Searching on Graphs – Search an entity in the graph.
    Traversal of Graphs – Traversing all the nodes in the graph.
*/
    
    /* 
    What I can do:
    Instead of primitive data types such as int or maybe referenced like String, Characters,
    use NODE data structure instead since NODE data structure could incorporate more features and methods
    */


    //initializing Adjacency list for Graph
    static ArrayList<ArrayList<Integer>> CreateAdjList(int vertices){
        ArrayList<ArrayList<Integer>> Graphs = new ArrayList<>();
        for (int i =0; i< vertices; i++){
            ArrayList<Integer> NewList = new ArrayList<>();
            Graphs.add(NewList);
        }
        return Graphs;
    }

    //This is for adding an edge to an undirected graph in Adjacency List
    static void AddEdge(ArrayList<ArrayList<Integer>> Graphs, int num1, int num2){
        Graphs.get(num1).add(num2);
        Graphs.get(num2).add(num1);
    }

    static void PrintGraph(ArrayList<ArrayList<Integer>> Graphs){
        for (int i=0; i<Graphs.size(); i++){
            System.out.println("Linked List for vertex " + i);
            for (int j=0; j<Graphs.get(i).size(); j++){
                System.out.print(Graphs.get(i).get(j) + " --> ");
            }
            System.out.println("");
        }
    }

    //Undirected Graph using Adjacency Matrix
    static int[][] AdjMatrix(int vertices){
        
        int[][] adjMat = new int[vertices + 1][vertices + 1];
        return adjMat;
    }

    static void MatrixAddEdge(int[][] matrix, int num1, int num2){
        matrix[num1][num2] = 1;
        matrix[num2][num1] = 1;

    }

    static void PrintMatrix(int[][] matrix){
        for (int i=0; i<matrix.length; i++){
            System.out.println("");
            for (int j=0; j<matrix[i].length; j++){
                System.out.print(matrix[i][j] + " ");
            }
        }

    }

        
    
    

    public static void main (String args[]){
        ArrayList<ArrayList<Integer>> Graph1 = CreateAdjList(10);
        AddEdge(Graph1, 4, 5);
        AddEdge(Graph1, 4, 6);
        PrintGraph(Graph1);

        int[][] Matrix1 = AdjMatrix(8);
        MatrixAddEdge(Matrix1, 8, 5);
        PrintMatrix(Matrix1);
    



    }
}