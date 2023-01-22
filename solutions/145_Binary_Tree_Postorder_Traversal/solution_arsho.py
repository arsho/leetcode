"""
Title     : 145. Binary Tree Postorder Traversal
Category  : Tree
URL       : https://leetcode.com/problems/binary-tree-postorder-traversal/
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

    def traverse(self, root):
        if root != None:
            self.traverse(root.left)
            self.traverse(root.right)
            self.result.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        self.traverse(current)
        return self.result