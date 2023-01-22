"""
Title     : 2460. Apply Operations to an Array
Category  : Array
URL       : https://leetcode.com/problems/apply-operations-to-an-array/
Author    : arsho
Created   : 21 January 2023
"""
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i, v in enumerate(nums):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        res = []
        for i, v in enumerate(nums):
            if v != 0:
                res.append(v)
        for i in range(len(nums) - len(res)):
            res.append(0)
        return res
