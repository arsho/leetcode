"""
Title     : 1768. Merge Strings Alternately
Category  : String
URL       : https://leetcode.com/problems/merge-strings-alternately/
Author    : arsho
Created   : 21 February 2021
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ""
        for i in range(min(len(word1), len(word2))):
            merged_word += word1[i]
            merged_word += word2[i]
        for i in range(min(len(word1), len(word2)), len(word1)):
            merged_word += word1[i]
        for i in range(min(len(word1), len(word2)), len(word2)):
            merged_word += word2[i]
        return merged_word
