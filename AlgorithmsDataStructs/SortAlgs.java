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

    static void BubbleSort(int array[]){
        int alength = array.length;
        boolean sorted = false;
        while (sorted == false){
            sorted = true;
            for (int i = 0; i < array.length - 1; i++){
                if (array[i] > array[i+1]){
                    int temp = array[i];
                    array[i] = array[i+1];
                    array[i+1] = temp;
                }
            }
        }
    }

    /*
    Time Complexity = O(n^2)
    Space Complexity = O(1)
    used for large datasets, though not efficient
    */
    public static void main (String args[]){
        int [] array = {4,1,2,5,6};
        //SelectionSort(array);
        BubbleSort(array);
        for (int i =0; i<array.length; i++){
            System.out.print(array[i]);
        }
    }
}