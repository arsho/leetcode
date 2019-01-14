'''
Title     : 215. Kth Largest Element in an Array
Category  : Divide and Conquer
URL       : https://leetcode.com/problems/kth-largest-element-in-an-array/
Author    : arsho
Created   : 14 January 2019
'''


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k - 1]
