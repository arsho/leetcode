"""
Title     : 275. H-Index II
Category  : Binary Search
URL       : https://leetcode.com/problems/h-index-ii/
Author    : arsho
Created   : 14 August 2020
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for i in range(len(citations), -1, -1):
            count = 0
            for j in range(len(citations) - 1, -1, -1):
                if citations[j] < i:
                    break
                count += 1
            if count >= i:
                return i
        return 0
