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
    public ListNode deleteDuplicates(ListNode head) {
        HashMap<Integer,Integer> hm = new HashMap<>();
        ListNode New = new ListNode();
        ListNode Next = new ListNode();
        int counter = 0;
        if (head == null){
            return null;
        }
        while (head != null){
            if (counter == 0){
                New.val = head.val;
                hm.put(head.val, 1);
                counter++;
            }
            else if (hm.containsKey(head.val)){
                int val = hm.get(head.val);
                hm.put(head.val, val + 1);
            } else {
                if (counter == 1){
                    Next.val = head.val;
                    New.next = Next;
                    hm.put(head.val, 1);
                } else {
                    //initializing next node
                    ListNode temp = new ListNode();
                    Next.next = temp;
                    Next = temp;

                    //connecting nodes together
                    Next.val = head.val;
                    hm.put(head.val,1);
                }
                counter++;
                
            }
            head = head.next;
        }

        return New;
    }
}