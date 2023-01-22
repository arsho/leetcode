"""
Title     : 104. Maximum Depth of Binary Tree
Category  : Tree
URL       : https://leetcode.com/problems/maximum-depth-of-binary-tree/
Author    : arsho
Created   : 21 January 2023
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
