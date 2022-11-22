public class Functions{ //recursions.  Remember, void used for methods that don't return, and datatype required for methods that return
    static void Gael(int value){
        String Statement = "We have now received intel on the number of " + value;
        System.out.println(Statement);
    }
    static int RecursiveSum(int value){
        if (value > 0){
            return value + RecursiveSum(value-1);
        } else{
            return 0;
        }     
    }
    static void ArraySum(int[]array){
        int total = 0;
        for (int i=0; i < array.length; i++){
            total += array[i];
        }
        System.out.println("Sum:" + " " + total);
    }
    static int Fibbonaci(int value){
        if (value > 1){
            return Fibbonaci(value-1) + Fibbonaci(value-2);
        }
        else if(value < 1){
            return 0;
        }
        else if (value == 1){
            return 1;
        }
        return value;
    }
   static int BinarySearch(int[]array,int target){
    int low = array[0];
    int high = array[array.length - 1];
    while (low < high){
        int mid = (low + high) / 2;
        if (array[mid] < target){
            low = mid + 1;
        }
        else if (array[mid] > target){
            high = mid - 1;
        }
        else if (array[mid] == target){
            return mid;
        }
    }
    return 0;
   }

   static int[] ManipulatedArray(int[]array){
    int[]array2 = new int[array.length + 1];
    for (int i =0;i<array.length;i++){
        if (array[i] >= array.length/2){
            array2[i] = array[i];
            array2[array2.length - 1] = 9000;
        }
    }
    for (int i : array2){
        System.out.println(String.format("x(%d)",i));
    }
    return array2;
   }

    public static void main(String args[]){
        Gael(79);
        System.out.println(RecursiveSum(79));
        int[]A1 = {1,2,4,5,1,2,5};
        int[]sorted = {1,2,3,4,5,6,7};
        ArraySum(A1);
        System.out.println(Fibbonaci(6));
        System.out.println(BinarySearch(sorted, 5));
    }
}