"""
Title     : 125. Valid Palindrome
Category  : String
URL       : https://leetcode.com/problems/valid-palindrome/
Author    : arsho
Created   : 03 August 2020
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c for c in s.lower() if c.isalnum()]
        return s == s[::-1]


# Alternative solution
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c for c in s.lower() if c.isalnum()]
        for i in range(len(s)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True
"""
