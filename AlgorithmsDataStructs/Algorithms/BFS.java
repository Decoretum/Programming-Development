package AlgorithmsDataStructs.Algorithms;

import java.util.*;
import java.util.LinkedList;

public class BFS {
    //BFS for Adjacency List
    public static void bfs (int number, ArrayList<LinkedList<Integer>> Graph){
        //since Java LinkedList implements Queu and DeQueu interfaces
        LinkedList<Integer> Queu = new LinkedList<>();
        ArrayList<Integer> Visited = new ArrayList<>();

        //By default, the selected node will be added to the Queu and visited
        Queu.addLast(number);
        Visited.add(number);

        //Queu will contain data that were not yet visited but will be visited later
        //so that their neighbors will also be traversed
        while (!Queu.isEmpty()){
            int current = Queu.poll();
            System.out.print(current + " ");

            //we iterate over the edges of a certain node
            int counter = 0;
            LinkedList<Integer> edges = Graph.get(current);
            

            //We traverse edges based on the chosen value from Queu
            while (counter < edges.size()){
                if (!Visited.contains(edges.get(counter))){
                    Visited.add(edges.get(counter));   
                    Queu.addLast(edges.get(counter));
                }
                counter++;
            }
        }


        
    }

    public static void addEdge(int a, int b, ArrayList<LinkedList<Integer>> Graph){
        Graph.get(a).add(b);
        //Graph.get(b).add(a);
    }

    public static ArrayList<LinkedList<Integer>> makeGraph (int length){
        ArrayList<LinkedList<Integer>> Container = new ArrayList<>();
        for (int i=0; i < length; i++){
            LinkedList<Integer> proxy = new LinkedList<>();
            Container.add(proxy);
        }
        return Container;
    }

    
    public static void main (String args[]){
        ArrayList<LinkedList<Integer>> Graph = makeGraph(7);
        //addEdge(4, 1, Graph);
        //addEdge(0, 4, Graph);
        addEdge(0, 1, Graph);
        addEdge(0, 2, Graph);
        addEdge(1, 2, Graph);
        addEdge(2, 0, Graph);
        addEdge(2, 3, Graph);
        addEdge(3, 3, Graph);
        // addEdge(1, 5, Graph);
        // addEdge(1, 6, Graph);
        bfs(2, Graph);
        System.out.println(Graph);
        
    }
}
