//https://www.tutorialspoint.com/data_structures_algorithms/index.htm
package AlgorithmsDataStructs;

public class SortAlgs{

    static void SelectionSort(int array[]){
        int alength = array.length;
        for (int i = 0; i < alength; i++){
            int min = i;
            for (int j = i+1; j < alength; j++){
                if (array[min] > array[j]){
                    min = j;
                }
            }
            int temp = array[min];
            array[min] = array[i];
            array[i] = temp;

        }
    }

    /*Selection Sort
    Time Complexity = O(n^2) since there are two nested loops 
    Space Complexity
    Auxiliary Space: O(1) as the only extra memory used is for temporary variables
    while swapping two values in Array. The selection sort never makes more than O(N) 
    swaps and can be useful when memory write is a costly operation.

    O(1) space complexity since space does not grow no matter the operations, loops, or input of data
    */
    public static void main (String args[]){
        int [] array = {4,1,2,5,6};
        SelectionSort(array);
        for (int i =0; i<array.length; i++){
            System.out.print(array[i]);
        }
    }
}