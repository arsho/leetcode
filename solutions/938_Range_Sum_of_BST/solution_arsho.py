"""
Title     : 938. Range Sum of BST
Category  : Tree
URL       : https://leetcode.com/problems/range-sum-of-bst/
Author    : arsho
Created   : 22 January 2023
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def get_sum(self, root):
        if root != None:
            if self.low <= root.val <= self.high:
                self.total += root.val
            if self.low <= root.val <= self.high:
                self.get_sum(root.left)
                self.get_sum(root.right)
            elif root.val < self.low:
                self.get_sum(root.right)
            elif root.val > self.high:
                self.get_sum(root.left)

    def rangeSumBST(self, root: Optional[TreeNode], low: int,
                    high: int) -> int:
        self.total = 0
        self.low = low
        self.high = high
        self.get_sum(root)
        return self.total
