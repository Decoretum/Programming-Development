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

    public static void miniFunc(ArrayList<LinkedList<Integer>> Graph, Stack<Integer> s, ArrayList<Integer> Visited, int index, int count ){
        while (!s.isEmpty()){
            //This is the current node popped 
            int current = s.pop();

            int chosen = Graph.get(current).get(count);
            if (!Visited.contains(chosen)){
                System.out.print(chosen + " ");
                s.add(chosen);
                index = 0;
            } else {
                index++;
            }
        }
    }

    public static void dfs (int number, ArrayList<LinkedList<Integer>> Graph){
        Stack<Integer> s = new Stack<>();
        ArrayList<Integer> Visited = new ArrayList<>();

        Visited.add(number);
        s.add(number);
        System.out.print(number + " ");

        //This will be dynamic
        int index = 0; 

        //This will be the counter
        int count = 0;

        //size of edges of chosen node
        int length = Graph.get(number).size();

        while (count < length){
            miniFunc(Graph, s, Visited, index, count);
            count++;

        //stack is  empty at this point
        }
        

        


    }
    public static void main (String args[]){
        ArrayList<LinkedList<Integer>> Graph =  makeGraph(4);
        addEdge(0, 1, Graph);
        addEdge(0, 2, Graph);
        addEdge(1, 2, Graph);
        addEdge(2, 0, Graph);
        addEdge(2, 3, Graph);
        addEdge(3, 3, Graph);

        dfs(2, Graph);
        System.out.println(Graph);
    }
}