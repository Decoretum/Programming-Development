package Leetcode;
import java.util.*;

public class LinkedList{

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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ArrayList<Integer> L1 = new ArrayList<>();
        ArrayList<Integer> L2 = new ArrayList<>();
        //for first List
        int val = l1.val;
        L1.add(0, val);
        while(l1.next != null){
            l1 = l1.next;
            val = l1.val;
            L1.add(0, val);
        }

        //for second list
        int val2 = l2.val;
        L2.add(0, val2);
        while(l2.next != null){
            l2 = l2.next;
            val2 = l2.val;
            L2.add(0, val2);
        }

        ArrayList<Integer> first = new ArrayList<>();
        ArrayList<Integer> second = new ArrayList<>();
        String s1 = "";
        String s2 = "";
        for (int i : L1){
            first.add(i);
        } 

        for (int i : L2){
            second.add(i);
        }
        for (int i : first){
            s1 += i;
        }
        for (int i : second){
            s2 += i;
        }

        
        if (s1.length() > s2.length()){
            int diff = s1.length() - s2.length();
            for (int i = 0; i != diff; i++){
                s2 = "0" + s2;
            }
        }
        else if(s2.length() > s1.length()){
            int diff = s2.length() - s1.length();
            for (int i = 0; i != diff; i++){
                s1 = "0" + s1;
            }
        }

        int carry = 0;
        int leftover = 0;
        String finals = "";

        for (int i = s1.length()-1; i >= 0; i--){
            String answer = "";
            if (carry == 0){
                 answer = String.valueOf(Integer.parseInt(String.valueOf(s1.charAt(i))) + Integer.parseInt(String.valueOf(s2.charAt(i))));
            }
            else if (carry != 0){
                 answer = String.valueOf(carry + Integer.parseInt(String.valueOf(s1.charAt(i))) + Integer.parseInt(String.valueOf(s2.charAt(i))));
            }
    
            if (answer.length() >= 2){
                carry = Integer.parseInt(String.valueOf(answer.charAt(0)));
                leftover = Integer.parseInt(String.valueOf(answer.charAt(1)));
                if (i == 0){
                    finals = String.valueOf(carry) + String.valueOf(leftover) + finals;
                }
                else{
                    finals = String.valueOf(leftover) + finals;
                }
            }
            else{
                carry = 0;
                finals = answer + finals;
            }
        }
        
        //The tricky section

        ListNode Current = new ListNode();
        ListNode Back = new ListNode();
        int i = finals.length()-1;

        if (finals.length() == 1){
            Current.val = Integer.parseInt(String.valueOf(finals.charAt(i)));
        }

        else{
            while (i >= 0){
            ListNode NewNode = new ListNode(Integer.parseInt(String.valueOf(finals.charAt(i))));
            ListNode Blank = new ListNode();
            if (i == finals.length()-1){
                NewNode.next = Blank;
                Current = NewNode;
                Back = NewNode;
                i--;
            }
            else if (i != finals.length()-1 && i > 0){
                Back.next = NewNode;
                NewNode.next = Blank;
                Back = NewNode;
                i--;
            }
            else{
                Back.next = NewNode;
                break;
                 }
            }

        }
        
               
        return Current;
    }
}
}