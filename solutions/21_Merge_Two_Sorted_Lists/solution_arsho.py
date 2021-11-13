'''
Title     : 21. Merge Two Sorted Lists
Category  : Linked List
URL       : https://leetcode.com/problems/merge-two-sorted-lists/
Author    : arsho
Created   : 06 May 2019
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        values = []
        while l1:
            values.append(l1.val)
            l1 = l1.next
        while l2:
            values.append(l2.val)
            l2 = l2.next
        values = sorted(values)
        if len(values) >= 1:
            res = ListNode(values[0])
            head = res
            for i in range(1, len(values)):
                node = ListNode(values[i])
                while head.next:
                    head = head.next
                head.next = node
            return res
        return None
