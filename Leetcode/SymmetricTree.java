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
    public boolean IsMeasure(TreeNode left, TreeNode right){
        if (left == null && right == null){
            return true;
        }
        if (left == null && right != null){
            return false;
        }
        if (right == null && left != null){
            return false;
        }
        
        return left.val == right.val && IsMeasure(left.left, right.right) && IsMeasure(left.right, right.left);
    }

    public boolean isSymmetric(TreeNode root) {
        
        if (root == null){
            return true;
        }

        return IsMeasure(root.left, root.right);
    }
}