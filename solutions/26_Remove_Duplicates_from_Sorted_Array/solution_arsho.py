"""
Title     : 26. Remove Duplicates from Sorted Array
Category  : Two Pointers
URL       : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Author    : arsho
Created   : 25 August 2020
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        i = 0
        nums_length = len(nums)
        while i < nums_length:
            nums[count] = nums[i]
            count += 1
            j = i + 1
            while j < nums_length and nums[i] == nums[j]:
                j += 1
            i = j
        return count
