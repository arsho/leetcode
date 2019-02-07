'''
Title     : 409. Longest Palindrome
Category  : Hash Table
URL       : https://leetcode.com/problems/longest-palindrome/
Author    : arsho
Created   : 07 February 2019
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        odd = []
        res = 0
        for c in d:
            if d[c] % 2 == 0:
                res += d[c]
            else:
                odd.append(d[c])
        odd = sorted(odd, reverse=True)
        if len(odd) <= 1:
            res += sum(odd)
        else:
            res += sum(odd) - (len(odd) - 1)
        return res
