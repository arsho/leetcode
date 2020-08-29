"""
Title     : 414. Third Maximum Number
Category  : Array
URL       : https://leetcode.com/problems/third-maximum-number/
Author    : arsho
Created   : 29 August 2020
"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_1 = None
        max_2 = None
        max_3 = None
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
                if max_1 is None or i > max_1:
                    max_3 = max_2
                    max_2 = max_1
                    max_1 = i
                elif max_2 is None or i > max_2:
                    max_3 = max_2
                    max_2 = i
                elif max_3 is None or i > max_3:
                    max_3 = i
        if max_3 is not None:
            return max_3
        return max_1


"""
# Alternative solution
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if len(nums) >= 3:
            return nums[-3]
        return nums[-1]
"""
