"""
Title     : 1470. Shuffle the Array
Category  : Array
URL       : https://leetcode.com/problems/shuffle-the-array/
Author    : arsho
Created   : 10 March 2021
"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ar = []
        for i in range(n):
            ar.append(nums[i])
            ar.append(nums[i + n])
        return ar
