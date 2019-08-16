'''
Title     : 83. Remove Duplicates from Sorted List
Category  : Linked List
URL       : https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Author    : arsho
Created   : 16 August 2019
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res = list(sorted(set(res), key=res.index))
        if len(res) > 0:
            root = ListNode(res[0])
            head = root
            for i in res[1:]:
                node = ListNode(i)
                while root.next:
                    root = root.next
                root.next = node
            return head
        return None