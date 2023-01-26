//https://www.tutorialspoint.com/data_structures_algorithms/index.htm

package AlgorithmsDataStructs;

public class SearchAlgs{
    static int LinSearch(int array[], int target){ //O(n) time complexity
        for (int i = 0; i < array.length; i++){
            if (array[i] == target){
                return i;
            }
        }
        return 1;
    }

    static void SentLinSearch(int array[], int target){
        int last = array[array.length-1];
        array[array.length-1] = target;
        int i = 0;
        while (array[i] != target){
            i++;
        }
        array[array.length-1] = last;
        System.out.println(String.format("Index is at %d",i));
    }

    static void BinSearch(int array[], int target){ //considering the array is sorted, O(logn) time complexity
        int high = array[array.length - 1];
        int low = array[0];
        while (low <= high){
            int mid = (high + low) / 2;
            if (array[mid] > target){
                high = mid - 1;
            }

            else if (array[mid] < target){
                low = mid + 1;
            }

            else if (array[mid] == target){
                System.out.println(mid);
                break;
            }
        }
    }
    
    public static void main (String args[]){
        int [] array = {1,2,3,4,5};
        BinSearch(array,3);
        SentLinSearch(array,2);
    }
}