"""
Title     : 338. Counting Bits
Category  : Dynamic Programming
URL       : https://leetcode.com/problems/counting-bits/
Author    : arsho
Created   : 16 November 2021
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        offset = 0
        dp = [0 for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            if i & (i - 1) == 0:
                offset = i
            dp[i] = dp[i - offset] + 1
        return dp
