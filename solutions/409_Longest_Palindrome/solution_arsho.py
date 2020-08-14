'''
Title     : 409. Longest Palindrome
Category  : Hash Table
URL       : https://leetcode.com/problems/longest-palindrome/
Author    : arsho
Created   : 07 February 2019
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d.get(c, 0)+1
        max_length = 0
        count_odd_occurrences = 0
        for c in d:
            occurrence = d[c]
            max_length += occurrence
            if occurrence%2 == 1:
                count_odd_occurrences += 1
        if count_odd_occurrences>0:
            max_length -= count_odd_occurrences
            max_length += 1
        return max_length
