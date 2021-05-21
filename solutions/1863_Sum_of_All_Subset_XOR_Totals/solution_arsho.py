"""
Title     : 1863. Sum of All Subset XOR Totals
Category  : Backtracking
URL       : https://leetcode.com/problems/sum-of-all-subset-xor-totals/
Author    : arsho
Created   : 22 May 2021
"""
from itertools import combinations
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        total = 0
        for i in range(1, len(nums) + 1):
            pairs = combinations(nums, i)
            for pair in pairs:
                pair = list(pair)
                temp = None
                for i in pair:
                    if temp == None:
                        temp = i
                    else:
                        temp = temp ^ i
                total += temp
        return total
