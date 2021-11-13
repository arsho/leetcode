/*
Title     : 701. Insert into a Binary Search Tree
Category  : Tree
URL       : https://leetcode.com/problems/insert-into-a-binary-search-tree/
Author    : arsho
Created   : 13 November 2021
*/
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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            root = new TreeNode(val);
            return root;
        }
        TreeNode node = root;
        insert(node, val);
        return root;
    }

    public void insert(TreeNode node, int val) {
        if (node == null) {
            node = new TreeNode(val);
            return;
        }
        if(val > node.val) {
            if (node.right == null) {
                node.right = new TreeNode(val);
                return;
            }
            insertIntoBST(node.right, val);
        }
        else {
            if (node.left == null) {
                node.left = new TreeNode(val);
                return;
            }
            insertIntoBST(node.left, val);
        }

    }

}