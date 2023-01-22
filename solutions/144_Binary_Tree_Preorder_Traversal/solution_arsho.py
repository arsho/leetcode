"""
Title     : 144. Binary Tree Preorder Traversal
Category  : Tree
URL       : https://leetcode.com/problems/binary-tree-preorder-traversal/
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

    def traverse(self, node):
        if node != None:
            self.result.append(node.val)
            self.traverse(node.left)
            self.traverse(node.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.result