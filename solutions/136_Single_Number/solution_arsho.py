"""
Title     : 136. Single Number
Category  : Hash Table
URL       : https://leetcode.com/problems/single-number/
Author    : arsho
Created   : 31 August 2020
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)


# Alternative solution
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:        
        occurrences = {}
        for i in nums:
            occurrences[i] = occurrences.get(i, 0) + 1
        for key in occurrences:
            if occurrences[key] == 1:
                return key
"""
