"""
Title     : 1313. Decompress Run-Length Encoded List
Category  : Array
URL       : https://leetcode.com/problems/decompress-run-length-encoded-list/
Author    : arsho
Created   : 30 May 2021
"""
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = []
        for i in range(0, len(nums), 2):
            decompressed += [nums[i + 1]] * nums[i]
        return decompressed
