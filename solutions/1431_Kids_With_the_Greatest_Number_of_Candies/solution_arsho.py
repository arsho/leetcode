"""
Title     : 1431. Kids With the Greatest Number of Candies
Category  : Array
URL       : https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
Author    : arsho
Created   : 04 May 2020
"""
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candie = max(candies)
        can_have_max_candie = []
        for candie in candies:
            can_have_max_candie.append(candie + extraCandies >= max_candie)
        return can_have_max_candie
