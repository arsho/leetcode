'''
Title     : 876. Middle of the Linked List
Category  : Linked List
URL       : https://leetcode.com/problems/middle-of-the-linked-list/
Author    : arsho
Created   : 06 May 2019
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count_nodes = 0
        temp = head
        temp2 = head
        while temp:
            temp = temp.next
            count_nodes += 1
        if count_nodes <= 1:
            return head
        mid_point = count_nodes // 2
        pos = 0
        while temp2:
            temp2 = temp2.next
            pos += 1
            if pos == mid_point:
                return temp2