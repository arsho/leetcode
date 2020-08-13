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
        citations = sorted(citations, reverse=True)
        total_papers = len(citations)
        for i in range(total_papers, -1, -1):
            eligible_papers = 0
            for j in range(total_papers):
                if citations[j] < i:
                    break
                eligible_papers += 1
            if eligible_papers >= i:
                return i
        return 0


"""
# Alternative solution using hash map

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        d = {}
        for citation in citations:
            for i in range(citation + 1):
                d[i] = d.get(i, 0) + 1
        for i in sorted(d.keys(), reverse=True):
            if d[i] >= i:
                return i
        return 0
"""