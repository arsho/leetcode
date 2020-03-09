"""
Title     : 1295. Find Numbers with Even Number of Digits
Category  : Array
URL       : https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
Author    : arsho
Created   : 22 December 2019
"""
from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([i for i in nums if len(str(i)) % 2 == 0])
