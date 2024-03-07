package AlgorithmsDataStructs.Algorithms;

class Solution {
    public void Sort(int[]arr){
        int size = arr.length;
        int mid = size / 2;
        int [] left = new int[mid];
        int [] right = new int[size-mid];

        int l = 0, r = 0;

        if (size == 1){
            return;
        } 

        for (; l < size; l++){
            if (l < mid){
                left[l] = arr[l];
            }
            else{
                right[r] = arr[l];
                r++;
            }
        }

        Sort(left);
        Sort(right);
        Merge(left, right, arr);
    }

    public void Merge(int[]left, int[]right, int[] arr){
        int leftsize = left.length;
        int rightsize = right.length;
        int g=0, l=0, r=0;

        while (l < leftsize && r < rightsize){
            if (left[l] < right[r]){
                arr[g] = left[l];
                l++;
                g++;
            }
            else if (left[l] > right[r]){
                arr[g] = right[r];
                r++;
                g++;
            }

            else if (left[l] == right[r]){
                arr[g] = left[l];
                arr[g+1] = right[r];
                g += 2;
                l++;
                r++;
            }
        }

        while (l < leftsize){
            arr[g] = left[l];
            l++;
            g++;
        }

        while (r < rightsize){
            arr[g] = right[r];
            g++;
            r++;
        }


    }

    public int[] sortArray(int[] nums) {
        int [] cop = nums;
        Sort(cop);
        return cop;
    }
}