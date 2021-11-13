"""
Title     : 1. Two Sum
Category  : Hash Table
URL       : https://leetcode.com/problems/two-sum/
Author    : arsho
Created   : 03 September 2020
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positions = {}
        for i, val in enumerate(nums):
            remain = target - val
            if remain in positions:
                return [positions[remain], i]
            else:
                positions[val] = i
