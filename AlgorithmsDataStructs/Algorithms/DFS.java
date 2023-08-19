import java.util.*;
import java.util.LinkedList;

public class DFS{
    public static void addEdge(int a, int b, ArrayList<LinkedList<Integer>> Graph){
        Graph.get(a).add(b);
    }

    public static ArrayList<LinkedList<Integer>> makeGraph (int length){
        ArrayList<LinkedList<Integer>> Container = new ArrayList<>();
        for (int i=0; i < length; i++){
            LinkedList<Integer> proxy = new LinkedList<>();
            Container.add(proxy);
        }
        return Container;
    }

    public static void recur(ArrayList<LinkedList<Integer>> Graph, int node, boolean visited[]){
        System.out.print(node + " ");
        visited[node] = true;
        for (int i = 0; i < Graph.get(node).size(); i++){
            if (!visited[Graph.get(node).get(i)]){
                recur(Graph, Graph.get(node).get(i), visited);
            }
        }
    }

    public static void iter(ArrayList<LinkedList<Integer>> Graph, Stack<Integer> s, int node, boolean visited[]){
        
        while (!s.isEmpty())
        {
            //popped node
            int popped = s.pop();
        
            //Visit popped node and mark it as visited
            if (visited[popped] == false){
                visited[popped] = true;
                System.out.print(popped + " ");
            }

            for (int i = Graph.get(popped).size()-1; i >= 0; i--){
                int chosen = Graph.get(popped).get(i);
                if (!visited[chosen]){
                    s.push(chosen);
                }
        }

        //iterate to the edges of the popped node (neighbors)
        // for (int i = 0; i < Graph.get(popped).size(); i++){
        //     int chosen = Graph.get(popped).get(i);
        //         if (visited[chosen] == false){
        //             //System.out.print(chosen + " ");
        //             s.push(chosen);
        //             for (int j = 0; j < Graph.get(chosen).size(); j++){
        //                 if (!visited[Graph.get(chosen).get(j)]){
        //                     s.push(Graph.get(chosen).get(j));
        //                 }
                        
        //             }
        //     }
        // }
    }

    }

    public static void dfs (int number, ArrayList<LinkedList<Integer>> Graph){
        boolean visited[] = new boolean[Graph.size()];

        Stack<Integer> s = new Stack<>();
        //recur(Graph, number, visited);
        s.push(number);
        iter(Graph, s, number, visited);
    }

    
    public static void main (String args[]){
        // ArrayList<LinkedList<Integer>> Graph =  makeGraph(4);
        // addEdge(0, 1, Graph);
        // addEdge(0, 2, Graph);
        // addEdge(1, 2, Graph);
        // addEdge(2, 0, Graph);
        // addEdge(2, 3, Graph);
        // addEdge(3, 3, Graph);

        ArrayList<LinkedList<Integer>> Graph =  makeGraph(6); 
          
        addEdge(0, 1, Graph);
        addEdge(0, 2, Graph);
        addEdge(1, 0, Graph);
        addEdge(1, 3, Graph);
        addEdge(2, 0, Graph);
        addEdge(2, 3, Graph);
        addEdge(3, 4, Graph);
        addEdge(3, 5, Graph);
        addEdge(4, 3, Graph);
        addEdge(5, 3, Graph); 

        dfs(0, Graph);
        System.out.println(Graph);
    }
}