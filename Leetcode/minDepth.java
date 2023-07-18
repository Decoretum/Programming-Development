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
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        int leftdepth = minDepth(root.left);
        int rightdepth = minDepth(root.right);
        if (leftdepth < rightdepth && leftdepth != 0){
            return leftdepth + 1;
        } else if (rightdepth < leftdepth && rightdepth != 0){
            return rightdepth + 1;
        } else if (rightdepth < leftdepth && rightdepth == 0){
            return leftdepth + 1;
        }
        //if left depth < rightdepth and left depth == 0
        return rightdepth + 1;
    }
}