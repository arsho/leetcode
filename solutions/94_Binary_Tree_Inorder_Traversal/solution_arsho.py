"""
Title     : 94. Binary Tree Inorder Traversal
Category  : Tree
URL       : https://leetcode.com/problems/binary-tree-inorder-traversal/
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

    def __init__(self):
        self.result = []

    def traverse(self, current):
        if current != None:
            self.traverse(current.left)
            self.result.append(current.val)
            self.traverse(current.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.result