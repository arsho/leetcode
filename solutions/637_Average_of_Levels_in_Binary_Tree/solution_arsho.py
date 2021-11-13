'''
Title     : 637. Average of Levels in Binary Tree
Category  : Tree
URL       : https://leetcode.com/problems/average-of-levels-in-binary-tree/
Author    : arsho
Created   : 11 January 2019
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        d = {}
        queue = [(root, 0)]
        while queue:
            element, current_level = queue.pop(0)
            if current_level in d:
                d[current_level].append(element.val)
            else:
                d[current_level] = [element.val]
            if element.left:
                queue.append((element.left, current_level + 1))
            if element.right:
                queue.append((element.right, current_level + 1))
        return [sum(ar) / len(ar) for key, ar in d.items()]
