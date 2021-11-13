'''
Title     : 590. N-ary Tree Postorder Traversal
Category  : Tree
URL       : https://leetcode.com/problems/n-ary-tree-postorder-traversal/
Author    : arsho
Created   : 15 January 2019
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        vals = []
        stack = [root]
        while stack:
            top = stack.pop()
            vals.append(top.val)
            stack += top.children
        return vals[::-1]
