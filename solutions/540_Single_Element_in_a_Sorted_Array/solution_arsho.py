"""
Title     : 540. Single Element in a Sorted Array
Category  : Binary Search
URL       : https://leetcode.com/problems/single-element-in-a-sorted-array/
Author    : arsho
Created   : 18 March 2021
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if mid % 2 != 0:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                left = mid + 2
        return nums[left]
