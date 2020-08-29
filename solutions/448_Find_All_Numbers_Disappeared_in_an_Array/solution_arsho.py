"""
Title     : 448. Find All Numbers Disappeared in an Array
Category  : Array
URL       : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Author    : arsho
Created   : 29 August 2020
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        unique_numbers = {}
        missing_numbers = []
        for i in nums:
            unique_numbers[i] = 1
        for i in range(1, len(nums) + 1):
            if i not in unique_numbers:
                missing_numbers.append(i)
        return missing_numbers
