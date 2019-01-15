'''
Title     : 700. Search in a Binary Search Tree
Category  : Tree
URL       : https://leetcode.com/problems/search-in-a-binary-search-tree/
Author    : arsho
Created   : 15 January 2019
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        queue = [root]
        while queue:
            top = queue.pop(0)
            if top.val == val:
                return top
            if top.left and val < top.val:
                queue.append(top.left)
            if top.right and val > top.val:
                queue.append(top.right)
        return None
