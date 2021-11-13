'''
Title     : 965. Univalued Binary Tree
Category  : Tree
URL       : https://leetcode.com/problems/univalued-binary-tree/
Author    : arsho
Created   : 07 January 2019
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        values = []
        queue = []
        queue.append(root)
        while queue:
            top = queue.pop(0)
            values.append(top.val)
            if top.left != None:
                queue.append(top.left)
            if top.right != None:
                queue.append(top.right)
        return len(set(values)) == 1
