"""
Title     : 1512. Number of Good Pairs
Category  : HashTable
URL       : https://leetcode.com/problems/number-of-good-pairs/
Author    : arsho
Created   : 29 July 2020
"""


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        number_of_good_pairs = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    number_of_good_pairs += 1
        return number_of_good_pairs
