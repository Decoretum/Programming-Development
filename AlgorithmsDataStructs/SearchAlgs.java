//https://www.tutorialspoint.com/data_structures_algorithms/index.htm

package AlgorithmsDataStructs;

public class SearchAlgs{
    static int LinSort(int array[], int target){
        for (int i = 0; i < array.length; i++){
            if (array[i] == target){
                return i;
            }
        }
        return 1;
    }
    public static void main (String args[]){
        int [] array = {1,2,3,4,5};
        System.out.println(LinSort(array,3));
    }
}