public class Stranger{
public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // i = 0
        // j = 0
        // length = 4
        // needed = length / 2 (odd)
        // needed = length / 2 - 1, length / 2 (even)

        int length = nums1.length + nums2.length;

        int i = 0;
        int j = 0;
        int neededIndex = length / 2;
        int previousItem = -1;
        int item = -1;
        while (i + j <= neededIndex) {
            previousItem = item;
            if (i == nums1.length) {
                item = nums2[j];
                j++;
            } else if (j == nums2.length) {
                item = nums1[i];
                i++;
            } else if (nums1[i] < nums2[j]) {
                item = nums1[i];
                i++;
            } else {
                item = nums2[j];
                j++;
            }
        }

        if (length % 2 != 0) {
            return item;
        }

        return 0.5 * (previousItem + item);
      }
    }
