"""
Title     : 1833. Maximum Ice Cream Bars
Category  : Array
URL       : https://leetcode.com/problems/maximum-ice-cream-bars/
Author    : arsho
Created   : 25 April 2021
"""
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total_icecream_bar = 0
        for cost in costs:
            if cost > coins or coins <= 0:
                break
            total_icecream_bar += 1
            coins -= cost
        return total_icecream_bar
