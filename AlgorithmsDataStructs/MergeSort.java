public class MergeSort{
    static void Sort(int [] array){
        int size = array.length;
        int middle = array.length / 2;
        int [] left = new int[middle];
        int [] right = new int[size - middle];

        int all = 0, r = 0;

        if (size == 1){
            return;
        }

        for (; all < size; all++){
            if (all < middle){
                left[all] = array[all];
            }
            else{
                right[r] = array[all];
                r++;
            }
        }

        Sort(left);
        Sort(right);
        Merge(left, right, array);
    }

    static void Merge(int[] left, int[] right, int []array){
        int leftsize = left.length;
        int rightsize = right.length;
        int p = 0, l = 0, r = 0;
        while (l < leftsize && r < rightsize){
            if (left[l] < right[r]){
                array[p] = left[l];
                p++;
                l++;
            }

            else if (right[r] < left[l]){
                array[p] = right[r];
                p++;
                r++;
            }
        }

        while (l < leftsize){
            array[p] = left[l];
            p++;
            l++;
        }

        while (r < rightsize){
            array[p] = right[r];
            p++;
            r++;
        }
    }
    public static void main (String args[]){
        int [] superlist = {5,1,1,2,0,0};
        Sort(superlist);
        for (int i : superlist){
            System.out.print(i + " ");
        }
    }
}