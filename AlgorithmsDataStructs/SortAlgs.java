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
    When memory space is limited because it makes the minimum possible number of swaps during sorting.

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

    /* Bubble Sort
    Time Complexity = O(n^2)
    Space Complexity = O(1)
    used for large datasets, though not efficient

    It works well with large datasets where the items are almost sorted because it takes only one iteration to detect whether the list is sorted or not. 
    But if the list is unsorted to a large extend then this algorithm holds good for small datasets or lists.
    This algorithm is fastest on an extremely small or nearly sorted set of data.
    */

    static void InsertionSort(int array[]){
        int alength = array.length;
        int j;
        for (int i = 0; i < alength; i++){
            j = i;
            while (j > 0 && array[j] < array[j-1]){
                int temp = array[j];
                array[j] = array[j-1];
                array[j-1] = temp;
                j -= 1;
            }
        }
    }

    /*Insertion Sort
    Time Complexity = O(n^2)
    Space Complexity = O(1)
    The usage of memory is a constraint as it has space complexity of O(1).
    Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted,
    only few elements are misplaced in complete big array.
     */

    public static void main (String args[]){
        int [] array = {4,1,2,5,6};
        //SelectionSort(array);
        //BubbleSort(array);
        InsertionSort(array);
        for (int i =0; i<array.length; i++){
            System.out.print(array[i]);
        }
    }
}