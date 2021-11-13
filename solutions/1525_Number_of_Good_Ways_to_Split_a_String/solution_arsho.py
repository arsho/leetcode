"""
Title     : 1525. Number of Good Ways to Split a String
Category  : String
URL       : https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
Author    : arsho
Created   : 27 July 2020
"""


class Solution:
    def numSplits(self, s: str) -> int:
        string_length = len(s)
        left = {}
        right = {}
        count = 0
        left[s[0]] = 1
        for i in range(1, string_length):
            right[s[i]] = right.get(s[i], 0) + 1

        for i in range(1, string_length):
            if len(left.keys()) == len(right.keys()):
                count += 1
            left[s[i]] = left.get(s[i], 0) + 1
            right[s[i]] -= 1
            if right[s[i]] == 0:
                del right[s[i]]
        return count
