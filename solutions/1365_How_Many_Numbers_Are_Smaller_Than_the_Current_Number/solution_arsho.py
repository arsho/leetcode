"""
Title     : 1365. How Many Numbers Are Smaller Than the Current Number
Category  : Hash Table
URL       : https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
Author    : arsho
Created   : 07 March 2020
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        d = {}
        nums_length = len(nums)
        for i in range(nums_length):
            if d.get(nums[i], None):
                res.append(d[nums[i]])
            else:
                count_smaller = 0
                for j in range(nums_length):
                    if i != j and nums[j] < nums[i]:
                        count_smaller += 1
                d[nums[i]] = count_smaller
                res.append(d[nums[i]])
        return res
