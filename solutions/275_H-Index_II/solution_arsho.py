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
        total_papers = len(citations)
        for i in range(total_papers, -1, -1):
            left = 0
            right = total_papers - 1
            while left <= right:
                mid = (left + right)//2
                if citations[mid] >= i:
                    right = mid-1
                elif citations[mid] < i:
                    left = mid+1
            if total_papers - left >= i:
                return i
        return 0

if __name__ == "__main__":
    solution = Solution()
    h_index = solution.hIndex([0,1,3,5,6])
    assert h_index == 3


"""
Alternative solution
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

"""