/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        //Using iterative inorder traversal
        //stack will be used
        Stack<TreeNode> stack = new Stack<>();
        Stack<TreeNode> stack2 = new Stack<>();
        ArrayList<Integer> one = new ArrayList<>();
        ArrayList<Integer> two = new ArrayList<>();
        ArrayList<Integer> null1 = new ArrayList<>();
        ArrayList<Integer> null2 = new ArrayList<>();
        boolean cond = true;

    //edge case
    if ((p == null && q != null) || (q == null & p!= null)) return false;

    while ((p != null || !stack.isEmpty()) && (q != null || !stack2.isEmpty())){
        ArrayList<Integer> temp1 = new ArrayList<>();
        ArrayList<Integer> temp2 = new ArrayList<>();

            while (p != null || q != null){
                if ((p == null && q != null) || (q == null && p != null))
                return false;

                if ((p.left == null && q.left != null) || (p.right == null && q.right != null))
                return false;

                stack.push(p);
                stack2.push(q);

                p = p.left;
                q = q.left;
                if (p == null){
                    null2.add(10001);
                } if (q == null){
                    null1.add(10001);
                }
        }


        //p node or q node is null at this point
        TreeNode peeked = stack.pop();
        TreeNode peeked2 = stack2.pop();
        one.add(peeked.val);
        two.add(peeked2.val);
        p = peeked.right;
        q = peeked2.right;

    }

    //testing
    if (one.equals(two) && null1.equals(null2)){
        cond = true;
    } else {
        return false;
    }

        return cond;
        
    }
}