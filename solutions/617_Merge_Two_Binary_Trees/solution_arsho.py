'''
Title     : 617. Merge Two Binary Trees
Category  : Tree
URL       : https://leetcode.com/problems/merge-two-binary-trees/
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
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        queue1 = [t1]
        queue2 = [t2]
        while queue1 and queue2:
            top1, top2 = queue1.pop(0), queue2.pop(0)
            if top1 and top2:
                val = top1.val + top2.val
                top1.val = val
                if not top1.left and top2.left:
                    top1.left = TreeNode(0)
                if not top1.right and top2.right:
                    top1.right = TreeNode(0)
                queue1.append(top1.left)
                queue1.append(top1.right)
                queue2.append(top2.left)
                queue2.append(top2.right)
        return t1
