"""
Title     : 111. Minimum Depth of Binary Tree
Category  : Tree
URL       : https://leetcode.com/problems/minimum-depth-of-binary-tree/
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left != None and root.right != None:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left == None and root.right != None:
            return self.minDepth(root.right) + 1
        elif root.left != None and root.right == None:
            return self.minDepth(root.left) + 1
        return 1
