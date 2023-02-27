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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode Merged = new ListNode();
        ListNode Head = new ListNode();
        ArrayList<Integer> Vals = new ArrayList<>();
        int count = 0;
        if (list1 == null && list2 == null){
            Head = null;
        }    

        while (list1 != null && list2 != null){
            if (list1.val > list2.val){
                Vals.add(list2.val);
                Vals.add(list1.val);
                count+=2;
            }

            else if (list1.val <= list2.val){
                Vals.add(list1.val);
                Vals.add(list2.val);
                count+=2;
            }

            list1 = list1.next;
            list2 = list2.next;
        }

        if (list1 != null){
            Vals.add(list1.val);
            count++;
            while (list1.next != null){
                list1 = list1.next;
                Vals.add(list1.val);
                count++;
            }
        }

        if (list2 != null){
            Vals.add(list2.val);
            count++;
            while (list2.next != null){
            list2 = list2.next;
            Vals.add(list2.val);
            count++;
            }
        }

        Collections.sort(Vals);
        int i = 0;
        while (i < count){
            if (i == 0){
                Head = Merged;
                Merged.val = Vals.get(i);
                if (i != count-1){
                    ListNode temp2 = new ListNode();
                    Merged.next = temp2;
                    Merged = Merged.next;
                }
            }
            
            else{
                Merged.val = Vals.get(i);
                if (i != count-1){
                    ListNode temp2 = new ListNode();
                    Merged.next = temp2;
                    Merged = Merged.next;
                }
            }
            i++;
        }
        System.out.println(Vals);
        return Head;
    }
}