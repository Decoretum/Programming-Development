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
    int counter = 0;
    public int depth(TreeNode node){
        if (node == null){
            return 0;
        }
        int leftdepth = depth(node.left);
        int rightdepth = depth(node.right);

        if (leftdepth > rightdepth){return leftdepth + 1;}
        else {return rightdepth + 1;}

    }

    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return depth(root);
    }
}