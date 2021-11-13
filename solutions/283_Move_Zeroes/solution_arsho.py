"""
Title     : 283. Move Zeroes
Category  : Array
URL       : https://leetcode.com/problems/move-zeroes/
Author    : arsho
Created   : 15 April 2020
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, value in enumerate(nums):
            if value == 0:
                for j in range(i + 1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break