"""
Title     : 2073. Time Needed to Buy Tickets
Category  : Array
URL       : https://leetcode.com/problems/time-needed-to-buy-tickets/
Author    : arsho
Created   : 14 November 2021
"""
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for i in range(len(tickets)):
            if i == k:
                count += tickets[k]
            elif i < k:
                count += min(tickets[i], tickets[k])
            elif i > k:
                count += min(tickets[i], tickets[k] - 1)
        return count
