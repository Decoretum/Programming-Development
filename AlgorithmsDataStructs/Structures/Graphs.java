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
    
    Distance of Vertices:
    Distance from vertex A to B

    Eccentricity of Vertices:
    Maximum distance that vertex A has to all other vertices

    Radius of a connected graph:
    Minimum value of eccentricity from all vertices

    Diameter of a connected graph:
    Maximum value of eccentricity from all vertices
    
    Central Point and Centre:
    Vertex that has minimum value of eccentricity is central point.
    Centre consists of sets of all central point.
    */


    //initializing Adjacency list for Graph
    static ArrayList<ArrayList<Node>> CreateAdjList(int vertices){
        ArrayList<ArrayList<Node>> Graphs = new ArrayList<>();
        for (int i =0; i< vertices; i++){
            ArrayList<Node> NewList = new ArrayList<>();
            Graphs.add(NewList);
        }
        return Graphs;
    }

    //This is for adding an edge to an undirected graph in Adjacency List
    static void AddEdge(ArrayList<ArrayList<Node>> Graphs, int num1, int num2){
        Node n1 = new Node(String.valueOf(num1));
        Node n2 = new Node(String.valueOf(num2));
        Graphs.get(num1).add(n2);
        Graphs.get(num2).add(n1);
    }

    static void PrintGraph(ArrayList<ArrayList<Node>> Graphs){
        for (int i=0; i<Graphs.size(); i++){
            System.out.println("Linked List for vertex " + i);
            for (int j=0; j<Graphs.get(i).size(); j++){
                Node Current = Graphs.get(i).get(j);
                System.out.print("--> " + Current.getData());
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
        ArrayList<ArrayList<Node>> Graph1 = CreateAdjList(10);
        AddEdge(Graph1, 4, 5);
        AddEdge(Graph1, 4, 6);
        AddEdge(Graph1, 4, 2);
        AddEdge(Graph1, 6, 2);
        PrintGraph(Graph1);

        int[][] Matrix1 = AdjMatrix(8);
        MatrixAddEdge(Matrix1, 8, 5);
        PrintMatrix(Matrix1);
    



    }
}