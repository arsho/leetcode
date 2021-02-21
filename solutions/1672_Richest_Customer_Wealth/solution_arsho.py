"""
Title     : 1672. Richest Customer Wealth
Category  : Array
URL       : https://leetcode.com/problems/richest-customer-wealth/
Author    : arsho
Created   : 21 February 2021
"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(ar) for ar in accounts])
