"""
Title     : 1752. Check if Array Is Sorted and Rotated
Category  : Array
URL       : https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
Author    : arsho
Created   : 14 March 2021
"""


class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            temp = nums[i:] + nums[:i]
            if temp == sorted(nums):
                return True
        return False
