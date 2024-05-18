"""
Title     : 14. Longest Common Prefix
Category  : String
URL       : https://leetcode.com/problems/longest-common-prefix/description/
Author    : arsho
Created   : 18 May 2024
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0
        c = ""
        while True:
            for s in strs:
                if c == "":
                    if i < len(s):
                        c = s[i]
                    else:
                        return prefix
                else:
                    if i < len(s) and c == s[i]:
                        continue
                    else:
                        return prefix
            prefix += c
            c = ""
            i += 1
