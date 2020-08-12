"""
Title     : 274. H-Index
Category  : Sort
URL       : https://leetcode.com/problems/h-index/
Author    : arsho
Created   : 12 August 2020
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        total_papers = len(citations)
        if total_papers == 0:
            return 0
        h_index = 0

        for i in range(1, total_papers + 1):
            eligible_papers = 0
            for j in range(total_papers):
                if citations[j] >= i:
                    eligible_papers = total_papers - j
                    break
            if eligible_papers >= i:
                h_index = i
        return h_index
