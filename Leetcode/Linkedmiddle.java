package Leetcode;
import java.util.*;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ArrayList<ListNode> check = new ArrayList<>();
        check.add(head);
        ListNode copy = head;
        while (head.next != null){
            head = head.next;
            check.add(head);
            
        }
        int length = check.size();
        int middle = length / 2;
        int count = 0;

        while(count != middle){
            copy = copy.next;
            count += 1;
        }
        System.out.println(count);
        System.out.print(middle);
        return copy;
    }
}