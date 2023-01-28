public class PalindromeList{
    public class ListNode {
     int val;
     ListNode next;
     ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }
    public boolean isPalindrome (String args[]){
        ListNode current = head;
        ArrayList <Integer> list = new ArrayList<>();
        ArrayList <Integer> newlist = new ArrayList<>();
        while (current != null){
            list.add(current.val);
            newlist.add(0,current.val);
            current = current.next;
        }
        if (newlist.equals(list) == true){
            return true;

        }
        else{
            return false;
        }
    }
    }
}