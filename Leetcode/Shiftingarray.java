public class Shiftingarray {
    static void duplicateZeros(int[] arr) {
        for (int i = 0; i < arr.length; ){
            if (arr[i] == 0){
                for (int j=arr.length-2; j>= i; j--){
                    arr[j + 1] = arr[j];
                }
                i += 2;
            }
            else{
                i +=1;
            }
        }
    }

    public static void main (String args[]){
        int[] testy = {1,0,2,3,0,4,5,0};
        duplicateZeros(testy);
        for (int i : testy){
            System.out.print(i + " ");
        }
    }
}