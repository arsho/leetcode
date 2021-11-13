"""
Title     : 1290. Convert Binary Number in a Linked List to Integer
Category  : Linked List
URL       : https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
Author    : arsho
Created   : 21 December 2019
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ar = []
        while head:
            ar.append(str(head.val))
            head = head.next
        s = "".join(ar)
        return int(s, 2)
