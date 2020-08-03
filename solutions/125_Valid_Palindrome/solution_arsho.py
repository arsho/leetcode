"""
Title     : 125. Valid Palindrome
Category  : String
URL       : https://leetcode.com/problems/valid-palindrome/
Author    : arsho
Created   : 03 August 2020
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join([c for c in s if c.isalnum()])
        return s == s[::-1]
