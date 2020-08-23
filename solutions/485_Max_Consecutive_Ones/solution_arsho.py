"""
Title     : 485. Max Consecutive Ones
Category  : Array
URL       : https://leetcode.com/problems/max-consecutive-ones/
Author    : arsho
Created   : 23 August 2020
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for i in nums:
            if i == 0:
                max_count = max(max_count, count)
                count = 0
            else:
                count += 1
        max_count = max(count, max_count)
        return max_count


    def findMaxConsecutiveOnesAlternative(self, nums: List[int]) -> int:
        s = "".join([str(i) for i in nums])
        ar = s.split("0")
        print(s, ar)
        m = 0
        for i in ar:
            m = max(m, len(i))
        return m
