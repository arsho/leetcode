"""
Title     : 169. Majority Element
Category  : Hash Table
URL       : https://leetcode.com/problems/majority-element/
Author    : arsho
Created   : 25 August 2021
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurrences = {}
        major = nums[0]
        for i in nums:
            occurrences[i] = occurrences.get(i, 0) + 1
            if occurrences[i] > len(nums) / 2:
                major = i
                break
        return major
